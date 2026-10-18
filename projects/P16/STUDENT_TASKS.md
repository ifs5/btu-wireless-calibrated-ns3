# P16 — Kalibre Coverage Gradient Boyunca Mobility: Uygulama Görevleri

**Proje:** Intermediate · **Zorunlu core:** 30 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Hareketli bir station calibrated coverage gradient boyunca ilerlerken performansı nasıl değişir?

**Birincil değişken:** `mobilitySpeedMps` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
STA0'ın +x doğrultusunda hareket ettiği, hız=0.5/1/1.5 m/s ve P0/P1 bulunan baseline hazır.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Sabit zaman aralığında STA pozisyonu ve teslim edilen byte sayacı; time-binned throughput ve gerekçeli outage threshold analizi geliştir.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
Zaman pencereleri çakışmadan ölçüm aralığını kaplar; bin byte toplamı aggregate byte ile tutarlı; pozisyon beklenen yönde ilerler; outage yoksa 0.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Bu tek-AP modelinde handover/roaming yoktur, hız otomatik outage anlamına gelmez.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
