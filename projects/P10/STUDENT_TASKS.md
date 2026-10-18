# P10 — Channel Width Trade-off: Uygulama Görevleri

**Proje:** Intermediate · **Zorunlu core:** 30 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Channel width 20 MHz’den 40/80 MHz’e çıkarıldığında ne zaman throughput artar ve ne zaman channel quality avantajı sınırlar?

**Birincil değişken:** `channelWidthMHz` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
20/40/80 MHz channel width senaryoları hazır.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Mbps/MHz normalize edilmiş verimlilik analizi yaz; genişlik/PHY uygulama ayarını çıktıdan doğrula; P0/P1 grafikleri üret.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
Birim testi Mbps/MHz doğru; PHY ayarında beklenen üç genişlik gerçekten uygulanmalı; diğer kontrol parametreleri sabit.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Offered-load sınırlı deneyden PHY'nin teorik maksimum kapasitesi çıkarılmaz.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
