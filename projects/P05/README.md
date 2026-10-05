# P05 — Kalibrasyon Gerçekten Fark Yaratıyor mu?

**Aile:** Propagation / Validation  
**Zorluk seviyesi:** Intermediate  
**Core run bütçesi:** yaklaşık 80 run

## Araştırma sorusu

Measurement-calibrated log-distance model, textbook `n=2` modele göre tahmin edilen received-performance trendlerini ne ölçüde değiştirir?

## Birincil factor

`propagation model`: P0, P1, P2, P3

## Zorunlu metric'ler

RSSI/received-power trend (mümkünse); throughput; PDR; delay; model sensitivity

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

Hold-out measurements ile RMSE validation ekleyin.

## Sınıf ortak araştırmasına katkısı

Calibration/validation makalesinin temel work package’ı.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
