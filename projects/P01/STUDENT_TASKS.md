# P01 — İstemci Yoğunluğu ve WLAN Doyumu: Uygulama Görevleri

**Proje:** Standard · **Zorunlu core:** 50 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Kalibre edilmiş iç mekân kanalında bağlı istasyon sayısı arttıkça aggregate throughput, delay, PDR ve fairness nasıl değişir?

**Birincil değişken:** `nSta` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
STA sayısı değişen tek AP ağı ve mevcut toplam KPI/Jain çıktısı hazır.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Her STA'nın kimlik ve throughput değerini CSV'ye yazan modülü geliştir; per-STA ve toplam throughput grafiğini üret; Jain indeksini per-STA çıktısından bağımsız doğrula.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
nSta=5 iken 5, nSta=40 iken 40 kimlik bulunmalı (paket almayan STA 0 ile yer almalı); per-STA toplamı aggregate ile eşleşmeli; eşit hız fixture'ında Jain=1.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Doyum veya P0/P1 farkı mutlaka gözlenecek diye PASS koşulu koyma.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
