# P15 — Yoğun 802.11ax Ortamında OFDMA: Uygulama Görevleri

**Proje:** Advanced · **Zorunlu core:** 20 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Aynı propagation koşullarında OFDMA hangi client-density düzeylerinde single-user scheduling’e göre avantaj sağlar?

**Birincil değişken:** `OFDMA` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
Eğitmen AP→çoklu STA **downlink** trafiği, HE standardı, P0/P1 ve OFDMA OFF çalışan asgari iskelet sağlamalı; henüz yok.

**Önemli:** Özel starter bu aşamada henüz hazırlanmadı/derlenmedi; eğitmen dağıtılabilir asgari iskeleti doğrulamadan tam uygulamaya başlanmaz.

## 3. Öğrencinin geliştireceği işlev
OFDMA ON/OFF için RrMultiUserScheduler bağlama mantığını kodla; istemci bazlı goodput/fairness topla; gerçek DL MU frame/PPDU trace kanıtı ekle.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
OFF scheduler yok; ON scheduler var; uygun yük altında gerçek DL MU frame saptanıyor; trafik AP→STA; 4 core senaryo × 5 run ayrı.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Mevcut STA→AP common starter'a OFDMA bayrağı eklemek DL OFDMA deneyi değildir.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
