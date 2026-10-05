# P11 — Rate Adaptation vs Sabit MCS

**Aile:** PHY / Configuration  
**Zorluk seviyesi:** Intermediate  
**Core run bütçesi:** yaklaşık 40 run

## Araştırma sorusu

Propagation kötüleştikçe adaptive rate selection, fixed MCS seçeneklerine göre ne kadar robust davranır?

## Birincil factor

`rateManager / dataMode`: ideal, fixed-low, fixed-mid, fixed-high

## Zorunlu metric'ler

throughput; PDR; delay

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

Her fixed mode’un viable olmaktan çıktığı mesafeyi belirleyin.

## Sınıf ortak araştırmasına katkısı

Rate-selection robustness’unun calibration’a duyarlılığı.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
