# P07 — Transmit Power, Coverage ve Verimlilik

**Aile:** Propagation / Coverage  
**Zorluk seviyesi:** Standard  
**Core run bütçesi:** yaklaşık 50 run

## Araştırma sorusu

Transmit power, calibrated channel altında kullanılabilir coverage bölgesini ve performansı nasıl değiştirir?

## Birincil factor

`txPowerDbm`: 8, 11, 14, 17, 20

## Zorunlu metric'ler

throughput; PDR; delay; coverage threshold

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

Performansı transmit power’a normalize edip energy trade-off’u tartışın.

## Sınıf ortak araştırmasına katkısı

Calibration altında Tx-power duyarlılığı.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
