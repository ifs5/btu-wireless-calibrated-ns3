# P11 — Rate Adaptation vs Sabit MCS: Uygulama Görevleri

**Proje:** Intermediate · **Zorunlu core:** 40 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Propagation kötüleştikçe adaptive rate selection, fixed MCS seçeneklerine göre ne kadar robust davranır?

**Birincil değişken:** `rateManager / dataMode` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
Ideal manager ve sabit HeMcs0/4/8 senaryoları matris içinde var; control-mode uyumluluğu henüz doğrulanmadı.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Geçerli data/control mode ayrımını ns-3.48'e uygun kur; gerçek data TX MCS/mode dağılımını PHY trace ile kaydet; fixed–ideal analizi geliştir.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
Sabit data mode gerçekten ilgili MCS; kontrol mode geçerli; ideal manager'ın seçimi gerçekte trace ile izleniyor; dört rate durumu × P0/P1 ayrı.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Yalnız CLI'de MCS adı görmek gerçek PHY modunu ispatlamaz.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
