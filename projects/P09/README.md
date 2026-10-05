# P09 — Ölçüm-Temelli Propagation ile 2.4 GHz vs 5 GHz

**Aile:** PHY / Propagation  
**Zorluk seviyesi:** Intermediate  
**Core run bütçesi:** yaklaşık 40 run

## Araştırma sorusu

Frequency-dependent 1 m reference loss ve measurement-informed distance exponent tutarlı ele alındığında 2.4 ve 5 GHz nasıl karşılaştırılır?

## Birincil factor

`bandGHz`: 2.4, 5.0

## Zorunlu metric'ler

throughput; PDR; delay; coverage trend

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

5-GHz exponent’i yeniden kullanmak yerine kontrollü bir 2.4-GHz reference dataset toplayıp fit edin.

## Sınıf ortak araştırmasına katkısı

Cross-band calibration metodolojisi.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
