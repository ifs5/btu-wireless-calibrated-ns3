# P13 — Yoğun Yükte Wi-Fi 5 vs Wi-Fi 6

**Aile:** Modern Wi-Fi  
**Zorluk seviyesi:** Intermediate  
**Core run bütçesi:** yaklaşık 40 run

## Araştırma sorusu

Aynı topology ve traffic altında client density arttıkça 802.11ac ve 802.11ax nasıl karşılaştırılır?

## Birincil factor

`standard`: ac, ax

## Zorunlu metric'ler

throughput; delay; PDR; fairness

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

İkinci bir channel width veya traffic profile ekleyin.

## Sınıf ortak araştırmasına katkısı

Standard comparison sonucunun calibrated propagation’a duyarlılığı.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
