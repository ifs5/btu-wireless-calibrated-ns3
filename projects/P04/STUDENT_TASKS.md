# P04 — Paket Boyutu ve MAC Verimliliği: Uygulama Görevleri

**Proje:** Standard · **Zorunlu core:** 50 run · **Durum:** Görev sözleşmesi; henüz çözüm kodu değildir.

## 1. Araştırma sorusu — eğitmen verdi
Aynı offered load altında application packet size WLAN verimliliğini ve güvenilirliğini nasıl etkiler?

**Birincil değişken:** `packetSize` — seçilecek seviyeler zaten [matrix.json](matrix.json) içinde verilmiştir. Bunları değiştirmenize gerek yok.

## 2. Eğitmenin sağlayacağı en küçük çalışan temel
Paket boyutu değişen UDP ağı ve toplu KPI hazır.

**Önemli:** Mevcut ortak ns-3 C++ kodu bulunmasına rağmen ns-3.48 compile/smoke-test henüz onaylanmadı.

## 3. Öğrencinin geliştireceği işlev
Payload byte/packet sayılarını ve offered/delivered byte oranını üreten ek sayaç/analiz geliştir; paket boyutuna göre goodput grafiği çiz.

Bu işlev için **kaynak kodu** ve kullanılan derleme/çalıştırma komutu saklanmalıdır; yalnız hazır script/matrix koşturmak tamamlanmış proje değildir.

## 4. Kabul testi
Known-byte fixture için Mbps hesabı doğru; 200 ve 1472 bayt etiketleri ayrışır; sıfır pakette bölme hatası yok.

Öğrenciler en az bir **pozitif** ve bir **sınır/olumsuz** durumun sonucunu raporlar. Testlerin kendi kodları özel gruba aittir; eğitmen burada çözümü vermiyor.

## 5. Çıktı ve açıklama
Kaynak kod değişiklikleri, kabul testi, dondurulmuş koşulara ait ham veri, en az bir proje grafiği, analizin yeniden üretme komutu, bilimsel yorum ve `AI_USAGE.md` private repo'ya konur.

**Dikkat:** Uygulama byte oranını gerçek MAC/PHY overhead diye sunma.

**Takvim:** 7. hafta teknik öngörü ve başlangıç demo; 8–11. hafta geliştirme ve test; 13. hafta final repo ve rapor.

Bağlantılar: [Konu açıklaması](README.md) · [Matrix](matrix.json) · [Tüm görevler](../../docs/STUDENT_WORK_CONTRACTS.md).
