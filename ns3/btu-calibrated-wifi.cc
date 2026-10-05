/*
 * SPDX-License-Identifier: GPL-2.0-only
 *
 * BTU Wireless Networks 2026-2027 starter simulation.
 * Target: ns-3.48 (single-AP infrastructure baseline).
 *
 * Purpose: provide a reproducible baseline that students modify as an
 * experimental instrument. It intentionally does not implement every project.
 */

#include "ns3/applications-module.h"
#include "ns3/core-module.h"
#include "ns3/flow-monitor-module.h"
#include "ns3/internet-module.h"
#include "ns3/mobility-module.h"
#include "ns3/network-module.h"
#include "ns3/wifi-module.h"

#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

using namespace ns3;

namespace
{

bool
FileExists(const std::string& path)
{
    std::ifstream f(path);
    return f.good();
}

WifiStandard
ParseStandard(const std::string& value)
{
    if (value == "n")
    {
        return WIFI_STANDARD_80211n;
    }
    if (value == "ac")
    {
        return WIFI_STANDARD_80211ac;
    }
    if (value == "ax")
    {
        return WIFI_STANDARD_80211ax;
    }
    if (value == "be")
    {
        return WIFI_STANDARD_80211be;
    }
    NS_FATAL_ERROR("Unsupported --standard=" << value << " (use n|ac|ax|be)");
    return WIFI_STANDARD_80211ax;
}

std::string
BandToken(double bandGHz)
{
    if (std::abs(bandGHz - 2.4) < 0.2)
    {
        return "BAND_2_4GHZ";
    }
    if (std::abs(bandGHz - 5.0) < 0.4)
    {
        return "BAND_5GHZ";
    }
    if (std::abs(bandGHz - 6.0) < 0.4)
    {
        return "BAND_6GHZ";
    }
    NS_FATAL_ERROR("Unsupported --bandGHz=" << bandGHz << " (use 2.4, 5, or 6)");
    return "BAND_5GHZ";
}

void
InstallPositions(NodeContainer staNodes,
                 NodeContainer apNode,
                 const std::string& topology,
                 const std::string& apPlacement,
                 double distanceM,
                 double mobilitySpeedMps)
{
    MobilityHelper apMobility;
    Ptr<ListPositionAllocator> apPositions = CreateObject<ListPositionAllocator>();

    Vector apPos{0.0, 0.0, 1.5};
    if (topology == "room")
    {
        if (apPlacement == "center")
        {
            apPos = Vector{10.0, 6.0, 1.5};
        }
        else if (apPlacement == "edge")
        {
            apPos = Vector{10.0, 0.5, 1.5};
        }
        else if (apPlacement == "corner")
        {
            apPos = Vector{0.5, 0.5, 1.5};
        }
        else
        {
            NS_FATAL_ERROR("For topology=room, apPlacement must be center|edge|corner");
        }
    }
    apPositions->Add(apPos);
    apMobility.SetPositionAllocator(apPositions);
    apMobility.SetMobilityModel("ns3::ConstantPositionMobilityModel");
    apMobility.Install(apNode);

    MobilityHelper staMobility;
    Ptr<ListPositionAllocator> staPositions = CreateObject<ListPositionAllocator>();
    if (topology == "ring")
    {
        const uint32_t n = staNodes.GetN();
        for (uint32_t i = 0; i < n; ++i)
        {
            constexpr double PI = 3.14159265358979323846;
            const double angle = (2.0 * PI * i) / std::max<uint32_t>(n, 1);
            staPositions->Add(Vector{distanceM * std::cos(angle),
                                     distanceM * std::sin(angle),
                                     1.0});
        }
    }
    else if (topology == "room")
    {
        // 20 m x 12 m oda için deterministik istemci grid yerleşimi.
        const uint32_t n = staNodes.GetN();
        const uint32_t cols = static_cast<uint32_t>(std::ceil(std::sqrt(static_cast<double>(n))));
        const double xStep = 18.0 / std::max<uint32_t>(cols - 1, 1);
        const uint32_t rows = static_cast<uint32_t>(std::ceil(static_cast<double>(n) / cols));
        const double yStep = 10.0 / std::max<uint32_t>(rows - 1, 1);
        for (uint32_t i = 0; i < n; ++i)
        {
            const uint32_t row = i / cols;
            const uint32_t col = i % cols;
            staPositions->Add(Vector{1.0 + col * xStep, 1.0 + row * yStep, 1.0});
        }
    }
    else
    {
        NS_FATAL_ERROR("Unsupported --topology=" << topology << " (use ring|room)");
    }
    staMobility.SetPositionAllocator(staPositions);
    if (mobilitySpeedMps > 0.0)
    {
        staMobility.SetMobilityModel("ns3::ConstantVelocityMobilityModel");
    }
    else
    {
        staMobility.SetMobilityModel("ns3::ConstantPositionMobilityModel");
    }
    staMobility.Install(staNodes);
    if (mobilitySpeedMps > 0.0 && staNodes.GetN() > 0)
    {
        Ptr<ConstantVelocityMobilityModel> moving = staNodes.Get(0)->GetObject<ConstantVelocityMobilityModel>();
        moving->SetVelocity(Vector{mobilitySpeedMps, 0.0, 0.0});
    }
}

} // namespace

int
main(int argc, char* argv[])
{
    std::string projectId{"P00"};
    std::string scenarioId{"baseline"};
    std::string modelLabel{"P1-calibrated"};
    std::string standardName{"ax"};
    std::string topology{"ring"};
    std::string apPlacement{"center"};
    std::string rateManager{"ideal"};
    std::string dataMode{"HeMcs4"};
    std::string outputCsv{"results.csv"};

    uint32_t nSta{10};
    uint32_t channelWidthMHz{20};
    uint32_t packetSize{1200};
    uint32_t seed{20261005};
    uint64_t run{1};
    bool enableRts{false};

    double bandGHz{5.0};
    double distanceM{8.0};
    double pathLossExponent{2.2};
    double referenceDistanceM{1.0};
    double referenceLossDb{46.427183}; // 1 m ve 5.0 GHz için Friis reference loss
    double txPowerDbm{18.0};
    double offeredLoadMbpsPerSta{2.0};
    double simulationTimeS{10.0};
    double mobilitySpeedMps{0.0};

    CommandLine cmd(__FILE__);
    cmd.AddValue("projectId", "Proje kimliği", projectId);
    cmd.AddValue("scenarioId", "Okunabilir senaryo kimliği", scenarioId);
    cmd.AddValue("modelLabel", "P0/P1/P2/P3 propagation etiketi", modelLabel);
    cmd.AddValue("standard", "Wi-Fi standard: n|ac|ax|be", standardName);
    cmd.AddValue("bandGHz", "Wi-Fi band: 2.4|5|6", bandGHz);
    cmd.AddValue("channelWidthMHz", "Channel width in MHz", channelWidthMHz);
    cmd.AddValue("nSta", "İstasyon sayısı", nSta);
    cmd.AddValue("topology", "ring|room", topology);
    cmd.AddValue("apPlacement", "center|edge|corner for room topology", apPlacement);
    cmd.AddValue("distanceM", "STA ring radius in metres", distanceM);
    cmd.AddValue("pathLossExponent", "Log-distance exponent n", pathLossExponent);
    cmd.AddValue("referenceDistanceM", "Log-distance reference distance", referenceDistanceM);
    cmd.AddValue("referenceLossDb", "Path loss at reference distance", referenceLossDb);
    cmd.AddValue("txPowerDbm", "Sabit Wi-Fi transmit power", txPowerDbm);
    cmd.AddValue("offeredLoadMbpsPerSta", "STA başına UDP offered load", offeredLoadMbpsPerSta);
    cmd.AddValue("packetSize", "Application payload size in bytes", packetSize);
    cmd.AddValue("enableRts", "Force RTS/CTS by setting RTS threshold to zero", enableRts);
    cmd.AddValue("rateManager", "ideal|constant", rateManager);
    cmd.AddValue("dataMode", "Constant-rate data mode when rateManager=constant", dataMode);
    cmd.AddValue("simulationTimeS", "Application measurement duration", simulationTimeS);
    cmd.AddValue("mobilitySpeedMps", "If >0, STA 0 moves along +x at this speed", mobilitySpeedMps);
    cmd.AddValue("seed", "ns-3 RNG seed", seed);
    cmd.AddValue("run", "ns-3 RNG run number", run);
    cmd.AddValue("outputCsv", "Append one result row to this CSV", outputCsv);
    cmd.Parse(argc, argv);

    if (nSta == 0 || simulationTimeS <= 0.0 || distanceM <= 0.0)
    {
        NS_FATAL_ERROR("nSta, simulationTimeS and distanceM must be positive");
    }

    if ((standardName == "ac") && bandGHz < 4.0)
    {
        NS_FATAL_ERROR("802.11ac baseline must use 5 GHz");
    }
    if ((standardName == "be") && bandGHz < 4.0)
    {
        NS_FATAL_ERROR("This starter uses 802.11be only on 5/6 GHz");
    }

    RngSeedManager::SetSeed(seed);
    RngSeedManager::SetRun(run);

    Config::SetDefault("ns3::WifiRemoteStationManager::RtsCtsThreshold",
                       UintegerValue(enableRts ? 0 : 999999));

    NodeContainer staNodes;
    staNodes.Create(nSta);
    NodeContainer apNode;
    apNode.Create(1);

    YansWifiChannelHelper channel;
    channel.SetPropagationDelay("ns3::ConstantSpeedPropagationDelayModel");
    channel.AddPropagationLoss("ns3::LogDistancePropagationLossModel",
                               "Exponent",
                               DoubleValue(pathLossExponent),
                               "ReferenceDistance",
                               DoubleValue(referenceDistanceM),
                               "ReferenceLoss",
                               DoubleValue(referenceLossDb));

    YansWifiPhyHelper phy;
    phy.SetChannel(channel.Create());
    phy.Set("TxPowerStart", DoubleValue(txPowerDbm));
    phy.Set("TxPowerEnd", DoubleValue(txPowerDbm));
    std::ostringstream channelSettings;
    channelSettings << "{0, " << channelWidthMHz << ", " << BandToken(bandGHz) << ", 0}";
    phy.Set("ChannelSettings", StringValue(channelSettings.str()));

    WifiHelper wifi;
    wifi.SetStandard(ParseStandard(standardName));
    if (rateManager == "ideal")
    {
        wifi.SetRemoteStationManager("ns3::IdealWifiManager");
    }
    else if (rateManager == "constant")
    {
        wifi.SetRemoteStationManager("ns3::ConstantRateWifiManager",
                                     "DataMode",
                                     StringValue(dataMode),
                                     "ControlMode",
                                     StringValue(dataMode));
    }
    else
    {
        NS_FATAL_ERROR("rateManager must be ideal|constant");
    }

    WifiMacHelper mac;
    Ssid ssid = Ssid("BTU-Calibrated-WiFi");
    mac.SetType("ns3::StaWifiMac", "Ssid", SsidValue(ssid), "ActiveProbing", BooleanValue(false));
    NetDeviceContainer staDevices = wifi.Install(phy, mac, staNodes);
    mac.SetType("ns3::ApWifiMac", "Ssid", SsidValue(ssid), "EnableBeaconJitter", BooleanValue(false));
    NetDeviceContainer apDevice = wifi.Install(phy, mac, apNode);

    int64_t stream = 1;
    stream += WifiHelper::AssignStreams(apDevice, stream);
    stream += WifiHelper::AssignStreams(staDevices, stream);

    InstallPositions(staNodes, apNode, topology, apPlacement, distanceM, mobilitySpeedMps);

    InternetStackHelper internet;
    internet.Install(staNodes);
    internet.Install(apNode);

    Ipv4AddressHelper ipv4;
    ipv4.SetBase("10.10.0.0", "255.255.0.0");
    Ipv4InterfaceContainer staIfs = ipv4.Assign(staDevices);
    Ipv4InterfaceContainer apIf = ipv4.Assign(apDevice);

    const uint16_t port = 5000;
    PacketSinkHelper sinkHelper("ns3::UdpSocketFactory",
                                InetSocketAddress(Ipv4Address::GetAny(), port));
    ApplicationContainer sinkApps = sinkHelper.Install(apNode.Get(0));
    sinkApps.Start(Seconds(0.5));
    sinkApps.Stop(Seconds(simulationTimeS + 2.0));

    const DataRate perStaRate(static_cast<uint64_t>(offeredLoadMbpsPerSta * 1e6));
    ApplicationContainer sources;
    for (uint32_t i = 0; i < nSta; ++i)
    {
        OnOffHelper onoff("ns3::UdpSocketFactory", InetSocketAddress(apIf.GetAddress(0), port));
        onoff.SetAttribute("PacketSize", UintegerValue(packetSize));
        onoff.SetAttribute("DataRate", DataRateValue(perStaRate));
        onoff.SetAttribute("OnTime", StringValue("ns3::ConstantRandomVariable[Constant=1]"));
        onoff.SetAttribute("OffTime", StringValue("ns3::ConstantRandomVariable[Constant=0]"));
        sources.Add(onoff.Install(staNodes.Get(i)));
    }
    sources.Start(Seconds(1.0));
    sources.Stop(Seconds(1.0 + simulationTimeS));

    FlowMonitorHelper flowHelper;
    Ptr<FlowMonitor> monitor = flowHelper.InstallAll();

    Simulator::Stop(Seconds(simulationTimeS + 2.0));
    Simulator::Run();
    monitor->CheckForLostPackets();

    Ptr<Ipv4FlowClassifier> classifier = DynamicCast<Ipv4FlowClassifier>(flowHelper.GetClassifier());
    const auto stats = monitor->GetFlowStats();

    uint64_t txPackets = 0;
    uint64_t rxPackets = 0;
    uint64_t rxBytes = 0;
    double delaySeconds = 0.0;
    std::vector<double> perFlowMbps;

    for (const auto& [flowId, st] : stats)
    {
        Ipv4FlowClassifier::FiveTuple tuple = classifier->FindFlow(flowId);
        if (tuple.protocol != 17 || tuple.destinationAddress != apIf.GetAddress(0) ||
            tuple.destinationPort != port)
        {
            continue;
        }
        txPackets += st.txPackets;
        rxPackets += st.rxPackets;
        rxBytes += st.rxBytes;
        delaySeconds += st.delaySum.GetSeconds();
        perFlowMbps.push_back((st.rxBytes * 8.0) / (simulationTimeS * 1e6));
    }

    const double throughputMbps = (rxBytes * 8.0) / (simulationTimeS * 1e6);
    const double pdrPct = txPackets > 0 ? (100.0 * rxPackets / txPackets) : 0.0;
    const double meanDelayMs = rxPackets > 0 ? (1000.0 * delaySeconds / rxPackets) : 0.0;

    double jain = 0.0;
    if (!perFlowMbps.empty())
    {
        const double sum = std::accumulate(perFlowMbps.begin(), perFlowMbps.end(), 0.0);
        double sumSq = 0.0;
        for (double x : perFlowMbps)
        {
            sumSq += x * x;
        }
        if (sumSq > 0.0)
        {
            jain = (sum * sum) / (perFlowMbps.size() * sumSq);
        }
    }

    const bool existed = FileExists(outputCsv);
    std::ofstream out(outputCsv, std::ios::app);
    if (!out)
    {
        NS_FATAL_ERROR("Could not open output CSV: " << outputCsv);
    }
    if (!existed)
    {
        out << "project_id,scenario_id,model_label,standard,band_ghz,channel_width_mhz,"
               "topology,ap_placement,n_sta,distance_m,path_loss_exponent,reference_loss_db,"
               "tx_power_dbm,offered_load_mbps_per_sta,packet_size,enable_rts,rate_manager,data_mode,"
               "mobility_speed_mps,seed,run,simulation_time_s,aggregate_throughput_mbps,pdr_pct,mean_delay_ms,jain_fairness\n";
    }
    out << std::fixed << std::setprecision(6)
        << projectId << ',' << scenarioId << ',' << modelLabel << ',' << standardName << ','
        << bandGHz << ',' << channelWidthMHz << ',' << topology << ',' << apPlacement << ',' << nSta
        << ',' << distanceM << ',' << pathLossExponent << ',' << referenceLossDb << ',' << txPowerDbm
        << ',' << offeredLoadMbpsPerSta << ',' << packetSize << ',' << (enableRts ? 1 : 0) << ','
        << rateManager << ',' << dataMode << ',' << mobilitySpeedMps << ',' << seed << ',' << run << ',' << simulationTimeS << ','
        << throughputMbps << ',' << pdrPct << ',' << meanDelayMs << ',' << jain << '\n';

    std::cout << "RESULT throughput_mbps=" << throughputMbps << " pdr_pct=" << pdrPct
              << " mean_delay_ms=" << meanDelayMs << " jain=" << jain << std::endl;

    Simulator::Destroy();
    return 0;
}
