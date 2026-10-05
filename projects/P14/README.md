# P14 — Karma Trafikte EDCA / QoS

**Aile:** QoS  
**Zorluk seviyesi:** Advanced  
**Core run bütçesi:** yaklaşık 20 run

## Araştırma sorusu

Best-effort traffic aynı calibrated WLAN için rekabet ederken EDCA delay-sensitive trafiği ne ölçüde korur?

## Birincil factor

`traffic mix / access category`: light-BE, heavy-BE

## Zorunlu metric'ler

per-class throughput; per-class delay; PDR

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

Resmî ns-3.48 `examples/wireless/wifi-multi-tos.cc` örneğinden başlayın. Eğitmen uyarlaması mixed ToS/EDCA traffic mekanizmasını koruyarak P0/P1 calibration ve ortak result schema eklemelidir. Ayrıntı: `../../docs/ADVANCED_STARTERS.md`.

## Optional +0…5 extension

Bir EDCA parametresini değiştirip mühendislik gerekçesini açıklayın.

## Sınıf ortak araştırmasına katkısı

Channel calibration altında QoS robustness.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.

> Bu specialized matrix bir deney spesifikasyonudur; common single-AP runner tarafından bilerek çalıştırılmaz.
