# P14 — Karma Trafikte EDCA / QoS: Uygulama Görevleri

**Proje:** Advanced · **Zorunlu core:** 20 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Best-effort traffic aynı calibrated WLAN için rekabet ederken EDCA delay-sensitive trafiği ne ölçüde korur?

**Birincil değişken:** `traffic mix / access category` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
Eğitmen QoS-capable AP–STA ve en az iki temel UDP akışı bulunan P0/P1 çalışan iskelet sağlamalı; henüz yok.

**Önemli:** Özel starter bu aşamada henüz hazırlanmadı/derlenmedi; eğitmen dağıtılabilir asgari iskeleti doğrulamadan tam uygulamaya başlanmaz.

## 3. Öğrencinin geliştireceği işlev
ToS/user priority→EDCA AC eşlemesini kodla; light/heavy BE offered load kontrolü ekle; trafik sınıfı bazlı gecikme/PDR/goodput ölç.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
AC etiketleri doğrulanır; yalnız BE yükü değişir; per-class sayıların toplamı tutarlı; voice mutlaka üstün olmalı koşulu yok.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** ToS alanını ayarlamak tek başına doğru QoS queue kullanıldığının kanıtı değildir.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
