# P03 — Hidden Terminal ve RTS/CTS

**Aile:** MAC / Contention  
**Zorluk seviyesi:** Intermediate  
**Core run bütçesi:** yaklaşık 20 run

## Araştırma sorusu

Textbook ve calibrated propagation altında hidden-terminal geometrisinde RTS/CTS hangi koşullarda performansı iyileştirir?

## Birincil factor

`enableRts`: 0, 1

## Zorunlu metric'ler

throughput; delay; PDR; retransmission/collision proxy

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

Resmî ns-3.48 `examples/wireless/wifi-simple-ht-hidden-stations.cc` örneğinden başlayın. Eğitmen uyarlaması P0/P1 calibration interface, ortak CSV result schema ve sabit hidden-node geometry sağlamalıdır. Ayrıntı: `../../docs/ADVANCED_STARTERS.md`.

## Optional +0…5 extension

RTS threshold veya hidden-node attenuation için ek sweep yapın.

## Sınıf ortak araştırmasına katkısı

RTS/CTS sonucunun channel calibration’a karşı robustness’u.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.

> Bu specialized matrix bir deney spesifikasyonudur; common single-AP runner tarafından bilerek çalıştırılmaz.
