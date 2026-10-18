# P13 — Yoğun Yükte Wi-Fi 5 vs Wi-Fi 6: Uygulama Görevleri

**Proje:** Intermediate · **Zorunlu core:** 40 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Aynı topology ve traffic altında client density arttıkça 802.11ac ve 802.11ax nasıl karşılaştırılır?

**Birincil değişken:** `standard` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
802.11ac/ax, 10/30 STA ve P0/P1 karşılaştırmalı ortak başlangıç hazır.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Uygulanan PHY/MAC ayarlarını raporlayan konfigürasyon audit aracı ve kontrollü standard/density kıyas analizi geliştir.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
İki standartta 5 GHz/20 MHz ve ilgili PHY modu geçerli; koşullar eşleşmiş; MU scheduler etkin değilse OFDMA kazancı iddia edilmiyor.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Wi-Fi 6'nın her koşulda daha iyi olacağı varsayılmaz.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
