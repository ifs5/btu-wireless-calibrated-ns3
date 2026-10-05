# P08 — Küçük İç Mekânda AP Yerleşimi

**Aile:** Topology / Planning  
**Zorluk seviyesi:** Intermediate  
**Core run bütçesi:** yaklaşık 30 run

## Araştırma sorusu

Sabit client layout için calibrated propagation altında hangi AP placement throughput/fairness açısından daha iyi sonuç verir?

## Birincil factor

`apPlacement`: center, edge, corner

## Zorunlu metric'ler

aggregate throughput; per-client throughput; PDR; Jain fairness

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

İkinci bir client-density pattern ekleyin.

## Sınıf ortak araştırmasına katkısı

Planning sonucunun calibration’a duyarlılığı.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
