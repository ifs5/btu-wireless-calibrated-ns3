# P09 — Ölçüm-Temelli Propagation ile 2.4 GHz vs 5 GHz: Uygulama Görevleri

**Proje:** Intermediate · **Zorunlu core:** 40 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Frequency-dependent 1 m reference loss ve measurement-informed distance exponent tutarlı ele alındığında 2.4 ve 5 GHz nasıl karşılaştırılır?

**Birincil değişken:** `bandGHz` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
2.4 ve 5 GHz ile ilgili matrix ve banda özgü 1 m Friis ref-loss placeholder'ları hazır.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Bant bazlı path-loss/parametre audit script'i ve aynı n varsayımında paired comparison analizi kodla.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
1 m için 5 GHz–2.4 GHz referans kayıp farkı yaklaşık 6.38 dB; bant/ReferenceLoss doğru eşleşmeli; yanlış '2.4 GHz'de ölçülmüş n' etiketi engellenmeli.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** 5 GHz sınıf n'si 2.4 GHz için ölçüme dayalı kanıt değil, kontrollü varsayımdır.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
