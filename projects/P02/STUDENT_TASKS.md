# P02 — Offered Load ve Doyum Eşiği: Uygulama Görevleri

**Proje:** Standard · **Zorunlu core:** 50 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Bir Wi-Fi hücresi hangi offered load seviyesinde unsaturated durumdan saturated duruma geçer ve propagation calibration bu sınırı değiştirir mi?

**Birincil değişken:** `offeredLoadMbpsPerSta` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
Offered-load parametresi ile UDP trafik kuran ortak baseline hazır.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Toplam offered load ile teslim edilen goodput'u ayrı hesapla; önceden belgelenmiş bir doyum/eşik algoritması yaz; iki propagation modeli için uygula.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
Offered load=nSta×STA başına load testi; sentetik doygun/doygun olmayan eğri testleri; eşik bulunmuyorsa 'gözlenmedi' sonucu.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Yük artınca delivered throughput'un otomatik arttığını varsayma.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
