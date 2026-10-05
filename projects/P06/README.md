# P06 — Mesafe ve Ağ Performansı

**Aile:** Propagation / Coverage  
**Zorluk seviyesi:** Standard  
**Core run bütçesi:** yaklaşık 50 run

## Araştırma sorusu

AP–client mesafesindeki artış, path loss üzerinden throughput, delay ve PDR’a nasıl yansır?

## Birincil factor

`distanceM`: 2, 5, 10, 15, 20

## Zorunlu metric'ler

throughput; delay; PDR; fairness

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

Kritik mesafelerde P2/P3 uncertainty bounds ekleyin.

## Sınıf ortak araştırmasına katkısı

Coverage boundary duyarlılığı.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
