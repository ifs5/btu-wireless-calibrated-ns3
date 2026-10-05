# P12 — İki WLAN Arasında Co-channel Interference

**Aile:** Interference / Topology  
**Zorluk seviyesi:** Advanced  
**Core run bütçesi:** yaklaşık 20 run

## Araştırma sorusu

Komşu same-channel BSS, separated-channel baseline’a göre performansı ne kadar düşürür ve calibration bu sonucu değiştirir mi?

## Birincil factor

`channel plan`: same-channel, separate-channel

## Zorunlu metric'ler

per-BSS throughput; delay; PDR; fairness

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

Resmî ns-3.48 `examples/wireless/wifi-simple-interference.cc` ve güncel Wi-Fi channel configuration yaklaşımından başlayın. P0/P1 calibration ve ortak result schema korunmalıdır. Ayrıntı: `../../docs/ADVANCED_STARTERS.md`.

## Optional +0…5 extension

BSS separation veya asymmetric load sweep yapın.

## Sınıf ortak araştırmasına katkısı

Co-channel sonucunun calibration’a duyarlılığı.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.

> Bu specialized matrix bir deney spesifikasyonudur; common single-AP runner tarafından bilerek çalıştırılmaz.
