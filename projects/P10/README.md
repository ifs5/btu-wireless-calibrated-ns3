# P10 — Channel Width Trade-off

**Aile:** PHY / Configuration  
**Zorluk seviyesi:** Intermediate  
**Core run bütçesi:** yaklaşık 30 run

## Araştırma sorusu

Channel width 20 MHz’den 40/80 MHz’e çıkarıldığında ne zaman throughput artar ve ne zaman channel quality avantajı sınırlar?

## Birincil factor

`channelWidthMHz`: 20, 40, 80

## Zorunlu metric'ler

throughput; delay; PDR; fairness

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

Near ve edge-of-coverage mesafelerinde tekrar edin.

## Sınıf ortak araştırmasına katkısı

Bandwidth/channel-quality etkileşimi.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
