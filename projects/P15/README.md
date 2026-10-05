# P15 — Yoğun 802.11ax Ortamında OFDMA

**Aile:** Modern Wi-Fi  
**Zorluk seviyesi:** Advanced  
**Core run bütçesi:** yaklaşık 20 run

## Araştırma sorusu

Aynı propagation koşullarında OFDMA hangi client-density düzeylerinde single-user scheduling’e göre avantaj sağlar?

## Birincil factor

`OFDMA`: off, on

## Zorunlu metric'ler

aggregate/per-user throughput; delay; fairness

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

Resmî ns-3.48 `examples/wireless/wifi-he-network.cc` örneğinden başlayın. Eğitmen uyarlaması HE/OFDMA scheduler mekanizmasını koruyarak P0/P1 calibration ve ortak result schema eklemelidir. Ayrıntı: `../../docs/ADVANCED_STARTERS.md`.

## Optional +0…5 extension

UL OFDMA veya BSRP’yi ikinci factor olarak ekleyin.

## Sınıf ortak araştırmasına katkısı

OFDMA faydasının channel calibration’a duyarlılığı.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.

> Bu specialized matrix bir deney spesifikasyonudur; common single-AP runner tarafından bilerek çalıştırılmaz.
