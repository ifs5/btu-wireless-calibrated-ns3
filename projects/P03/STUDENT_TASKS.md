# P03 — Hidden Terminal ve RTS/CTS: Uygulama Görevleri

**Proje:** Intermediate · **Zorunlu core:** 20 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Textbook ve calibrated propagation altında hidden-terminal geometrisinde RTS/CTS hangi koşullarda performansı iyileştirir?

**Birincil değişken:** `enableRts` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
Eğitmen çalışır iki hidden STA→AP, RTS kapalı, P0/P1 ve UDP akışı olan minimal ns-3.48 iskeleti sağlamalı; henüz yok.

**Önemli:** Özel starter bu aşamada henüz hazırlanmadı/derlenmedi; eğitmen dağıtılabilir asgari iskeleti doğrulamadan tam uygulamaya başlanmaz.

## 3. Öğrencinin geliştireceği işlev
RTS/CTS açık-kapalı anahtarını MAC ayarına bağla; uygun retransmission/drop trace'inden olay sayacı veya güvenilir proxy geliştir; topoloji varsayımını doğrula.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
STA'lar AP'ye erişebilmeli ve birbirlerine hidden olmalı; RTS ON/OFF trace ile doğrulanmalı; loss çakışma sayısı diye adlandırılmamalı; 4×5 core koşul ayrışmalı.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** FlowMonitor packet loss, doğrudan collision count değildir.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
