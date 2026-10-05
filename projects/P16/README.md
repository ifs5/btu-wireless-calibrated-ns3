# P16 — Kalibre Coverage Gradient Boyunca Mobility

**Aile:** Mobility / Propagation  
**Zorluk seviyesi:** Intermediate  
**Core run bütçesi:** yaklaşık 30 run

## Araştırma sorusu

Hareketli bir station calibrated coverage gradient boyunca ilerlerken performansı nasıl değişir?

## Birincil factor

`mobilitySpeedMps`: 0.5, 1.0, 1.5

## Zorunlu metric'ler

throughput; PDR; delay over run; outage/edge behavior

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

İkinci bir trajectory veya P2/P3 uncertainty ekleyin.

## Sınıf ortak araştırmasına katkısı

Mobility/outage duyarlılığının calibration’a etkisi.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
