# P01 — İstemci Yoğunluğu ve WLAN Doyumu

**Aile:** MAC / Contention  
**Zorluk seviyesi:** Standard  
**Core run bütçesi:** yaklaşık 50 run

## Araştırma sorusu

Kalibre edilmiş iç mekân kanalında bağlı istasyon sayısı arttıkça aggregate throughput, delay, PDR ve fairness nasıl değişir?

## Birincil factor

`nSta`: 5, 10, 20, 30, 40

## Zorunlu metric'ler

aggregate throughput; mean delay; PDR; Jain fairness

## Ortak zorunluluk

En az **P0 textbook propagation** (`n=2`) ile **P1 class-calibrated propagation** (`n=median`) karşılaştırılmalıdır. Frozen seed/run politikası kullanılmalı ve raw CSV sonuçları korunmalıdır.

## Starter

`common` starter (`ns3/btu-calibrated-wifi.cc`)

## Optional +0…5 extension

İki offered-load seviyesi ekleyerek saturation boundary’yi belirleyin.

## Sınıf ortak araştırmasına katkısı

Propagation calibration’a karşı yoğunluk duyarlılığı.

Core experiment matrix için `matrix.json` dosyasını kullanın. Core matrix üzerinde onaysız değişiklik yapmayın.
