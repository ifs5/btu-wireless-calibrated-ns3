# P07 — Transmit Power, Coverage ve Verimlilik: Uygulama Görevleri

**Proje:** Standard · **Zorunlu core:** 50 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Transmit power, calibrated channel altında kullanılabilir coverage bölgesini ve performansı nasıl değiştirir?

**Birincil değişken:** `txPowerDbm` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
8 m sabit uzaklık, 8/11/14/17/20 dBm güç durumları ve KPI hazır.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Bu **8 m koşulunda** önceden açıklanmış PDR hedefine ulaşan en düşük Tx power'ı bulan kod ve received-power değişimi denetimi yaz.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
Tx power +3 dB ise teorik received power +3 dB; uygun koşul yoksa 'gözlenmedi'; kullanılan mesafe çıktıda 8 m.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Bu çekirdek deney kapsama yarıçapını ya da enerji tüketimini ölçmüyor; bunlar ancak ek deney konusu.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
