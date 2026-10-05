# P04 — Paket Boyutu ve MAC Verimliliği

**Aile:** MAC / Traffic  
**Zorluk seviyesi:** Standard  
**Core run bütçesi:** yaklaşık 50 run

## Araştırma sorusu

Aynı offered load altında application packet size WLAN verimliliğini ve güvenilirliğini nasıl etkiler?

## Birincil factor

`packetSize`: 200, 500, 800, 1200, 1472

## Zorunlu metric'ler

throughput; delay; PDR; fairness

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

İkinci bir load seviyesinde deneyi tekrarlayın.

## Sınıf ortak araştırmasına katkısı

Calibrated channel altında packet-size etkisi.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
