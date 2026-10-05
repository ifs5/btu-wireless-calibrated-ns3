# Özel / İleri Starter Stratejisi

Ortak `ns3/btu-calibrated-wifi.cc` çoğu projeyi kapsar. P03, P12, P14 ve P15 ise ilgili Wi-Fi mekanizmasını tek-AP baseline içinde yapay biçimde taklit etmek yerine resmî ns-3 örneklerinden başlar. Amaç öğrencinin zamanı altyapıyı sıfırdan kurmaya değil, araştırma sorusuna ayırmasıdır.

## P03 — Hidden Terminal / RTS-CTS

Birincil resmî başlangıç noktası:

- `examples/wireless/wifi-simple-ht-hidden-stations.cc`
- Doxygen: https://www.nsnam.org/doxygen/d0/d7f/wifi-simple-ht-hidden-stations_8cc_source.html

Eğitmen uyarlaması:

- propagation kurulumunu dersin P0/P1 calibrated log-distance yapısıyla değiştirmek;
- hidden-node geometry'yi sabitlemek;
- ortak result-schema CSV alanlarını üretmek;
- RTS/CTS durumunu proje factor'ü olarak dışarı açmak.

## P12 — İki BSS Arasında Co-channel Interference

Yararlı resmî referanslar:

- Wi-Fi user documentation / channel configuration;
- `examples/wireless/wifi-simple-interference.cc`;
- yalnız frekans-overlap etkilerini daha ayrıntılı modellemek gerekiyorsa `SpectrumWifiPhy` değerlendirilmelidir.

Core karşılaştırma: same-channel vs separate-channel BSS. Topology sabit tutulmalıdır.

## P14 — EDCA / QoS

Birincil resmî başlangıç noktası:

- `examples/wireless/wifi-multi-tos.cc`
- `OnOffApplication` IPv4 `Tos` alanını destekler; trafik Wi-Fi QoS access category'lerine eşlenebilir.

Eğitmen starter'ı bir delay-sensitive flow class ve bir best-effort class'ı hazır kurmalıdır. Öğrenci tüm EDCA implementasyonunu yeniden yazmak yerine BE load'u değiştirir.

## P15 — OFDMA

Birincil resmî başlangıç noktası:

- `examples/wireless/wifi-he-network.cc`
- `WifiMacHelper::SetMultiUserScheduler("ns3::RrMultiUserScheduler", ...)`

Core scope: iki client-density seviyesi altında DL OFDMA off vs on; aynı P0/P1 propagation çifti kullanılır. UL OFDMA/BSRP yalnız optional extension kapsamındadır.

## Wi-Fi 7 MLO

MLO zorunlu proje değildir; setup ve doğrulama yükü diğer projelerden belirgin biçimde yüksektir. Uygun bir grup core projesini reproducible biçimde tamamladıktan sonra +0…5 extension olarak değerlendirilebilir.
