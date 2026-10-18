# P08 — Küçük İç Mekânda AP Yerleşimi: Uygulama Görevleri

**Proje:** Intermediate · **Zorunlu core:** 30 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Sabit client layout için calibrated propagation altında hangi AP placement throughput/fairness açısından daha iyi sonuç verir?

**Birincil değişken:** `apPlacement` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
20×12 m sanal oda, STA grid ve AP center/edge/corner konumları zaten tanımlı; AP taşınmıyor.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
STA ID–(x,y)–throughput/PDR kayıt kodu ile üç yerleşimin mekânsal performans haritalarını geliştir.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
Üç AP konumu farklı, bütün STA konumları aynı kalmalı; kayıt sayısı nSta; per-STA toplamı aggregate ile uyuşmalı.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Mevcut model duvar/mobilya içermiyorsa 'gerçek binadaki optimum yer' iddiası yok.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
