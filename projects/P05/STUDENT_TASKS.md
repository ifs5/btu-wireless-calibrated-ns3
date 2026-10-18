# P05 — Kalibrasyon Gerçekten Fark Yaratıyor mu?: Uygulama Görevleri

**Proje:** Intermediate · **Zorunlu core:** 80 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Measurement-calibrated log-distance model, textbook n=2 modele göre tahmin edilen received-performance trendlerini ne ölçüde değiştirir?

**Birincil değişken:** `propagation model` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
P0/P1/P2/P3 ve mesafe kombinasyonlarının 80 core run'ı matris içinde hazır.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Log-distance path-loss kestirim kodunu yaz; dört modelin teorik sinyal ve ağ-KPI duyarlılığını eşleştir; ölçülmüş hold-out varsa bağımsız RMSE ekle.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
d=d0 için loss=ReferenceLoss; mesafe 10× olunca loss 10n dB yükselir; dört modelin 80 run'ı eksiksiz; hold-out yoksa RMSE 'uygulanamaz'.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** P2/P3 belirsizlik duyarlılığıdır, %95 CI değildir; simülasyon-simülasyon karşılaştırması saha validasyonu değildir.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
