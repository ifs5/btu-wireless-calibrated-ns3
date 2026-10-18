# P06 — Mesafe ve Ağ Performansı: Uygulama Görevleri

**Proje:** Standard · **Zorunlu core:** 50 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
AP–client mesafesindeki artış, path loss üzerinden throughput, delay ve PDR’a nasıl yansır?

**Birincil değişken:** `distanceM` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
2/5/10/15/20 m mesafe karşılaştırmalı ortak ağ hazır.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Mesafe-KPI analiz modülü ve önceden seçilmiş PDR eşiğine göre en uzak deney noktasını bulan program geliştir.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
Hiç eşik karşılanmıyorsa 'gözlenmedi'; her nokta karşılıyorsa 'en fazla test edilen mesafe' döner; farklı model etiketleri karışmaz.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Denemediğin uzaklıklar için kesin kapsama yarıçapı iddia etme.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
