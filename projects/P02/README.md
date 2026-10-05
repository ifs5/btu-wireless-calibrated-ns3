# P02 — Offered Load ve Doyum Eşiği

**Aile:** MAC / Traffic  
**Zorluk seviyesi:** Standard  
**Core run bütçesi:** yaklaşık 50 run

## Araştırma sorusu

Bir Wi-Fi hücresi hangi offered load seviyesinde unsaturated durumdan saturated duruma geçer ve propagation calibration bu sınırı değiştirir mi?

## Birincil factor

`offeredLoadMbpsPerSta`: 0.5, 1, 2, 4, 8

## Zorunlu metric'ler

throughput; delay; PDR; fairness

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

Knee point’i algoritmik olarak tahmin edip P0/P1’i karşılaştırın.

## Sınıf ortak araştırmasına katkısı

Saturation-boundary duyarlılığı.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
