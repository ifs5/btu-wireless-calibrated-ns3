# P12 — İki WLAN Arasında Co-channel Interference: Uygulama Görevleri

**Proje:** Advanced · **Zorunlu core:** 20 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Komşu same-channel BSS, separated-channel baseline’a göre performansı ne kadar düşürür ve calibration bu sonucu değiştirir mi?

**Birincil değişken:** `channel plan` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
Eğitmen iki AP, onlara bağlı STA'lar, aynı-kanal UDP ve P0/P1 içeren minimum iki-BSS iskeleti sağlamalı; henüz yok.

**Önemli:** Özel starter bu aşamada henüz hazırlanmadı/derlenmedi; eğitmen dağıtılabilir asgari iskeleti doğrulamadan tam uygulamaya başlanmaz.

## 3. Öğrencinin geliştireceği işlev
Same/separate channel planını uygula, gerçek BSSID/association kontrolü ekle, BSS başına throughput/PDR CSV üret.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
Ayrı BSSID ve STA kümeleri doğrulanır; kanal örtüşmesi duruma uygun; per-BSS sayaçların toplamı tutarlıdır.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Resmî wifi-simple-interference örneği hazır iki-BSS projesi değildir; iskelet gelmeden öğrenciden çözümü bekleme.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
