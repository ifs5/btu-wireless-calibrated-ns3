# Dönem Projesi Öneri Formu

**Week 5 teslimi.** Bu form final rapor değildir; research question, measurement audit, deney planı ve uygulanabilirliği erkenden netleştirmek için kullanılır.

## A. Grup bilgileri

- Grup adı / kodu:
- Öğrenci 1 - Ad Soyad / No:
- Öğrenci 2 - Ad Soyad / No:
- Private GitHub repo adı:
- Public starter commit/tag:

## B. Proje tercihleri

| Tercih | Project ID | Proje adı | Kısa gerekçe |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

Nihai atama, sınıf genelinde yük/zorluk dengesi gözetilerek eğitmen tarafından yapılır.

## C. Eski laboratuvar ölçüm kaynağı (proje grubunun kendi n değeri değildir)

Eski ölçümler 5 kişilik **L01–L06** gruplarına aittir; yeni iki kişilik proje grubu eski veri dosyasını bağımsız yeni ölçüm diye çoğaltmaz. Kendi n değerinizi P1 olarak seçmeyin. P1/P2/P3 eğitmenin Week 6'da yayımladığı sınıf sürümünden alınır.

- Eski laboratuvar grubu kodu (L01–L06):
- 3. hafta LOS ölçüm dosyası:
- Ölçüm bandı/BSSID/rota (biliniyorsa):
- RSSI dBm var mı; mesafe/tekrar sayısı:
- Bilinen eksik/kalite problemi:

## C1. Önceki formdan ek denetim alanları

- Kullanılacak measurement dosyası:
- Ölçüm ortamı / yaklaşık konum:
- Band ve BSSID tutarlılığı:
- Kullanılan cihaz(lar):
- Mesafe noktaları ve tekrar sayısı:
- Eksik/şüpheli veri var mı?
- İlk `n` tahmini varsa:

> **Not:** Measurement intercept `A`, doğrudan ns-3 `ReferenceLoss` değildir. Ortak pipeline ölçümden `n` değerini kullanır; `ReferenceLoss` frekansa uygun 1 m Friis değeri ile tanımlanır.

## D. Araştırma sorusu ve hipotez

- Research question:
- Test edilebilir hipotez:
- Neden önemli?

## E. Deney tasarımı

P05 seçilirse P0/P1/P2/P3 core zorunludur. Diğer projelerde P0/P1 zorunludur. Core run sayısını public repo'daki atanmış matrix belirler.

- Birincil independent variable:
- Zorunlu P0/P1 karşılaştırması: P0 textbook ve P1 class-calibrated
- Sabit tutulacak değişkenler:
- Primary KPI:
- Diğer metric'ler:
- Core case sayısı:
- Her case için run sayısı:
- Tahmini toplam core run:
- Optional extension fikri (zorunlu değil):

## F. Calibration ve validation planı

1. Eski L-grubunuzun 3. hafta LOS ölçüm kaynağı nedir? Varsa eksiklerini belirtin.
2. P0 (n=2) ve eğitmen tarafından duyurulacak P1 (sınıf medyanı) arasında ne tür bir fark bekliyorsunuz?
3. Calibration sonucunun network-level conclusion'ı değiştirmediği bir sonuç da bilimsel olarak neden anlamlı olabilir?

## G. Reproducibility planı

- [ ] ns-3.48 kullanılacak.
- [ ] Starter commit/tag private repo'da kaydedilecek.
- [ ] Frozen matrix korunacak.
- [ ] Raw CSV dosyaları elle değiştirilmeden saklanacak.
- [ ] Figure üretme script/notebook'u saklanacak.
- [ ] `AI_USAGE.md` tutulacak.

## H. İş bölümü

| Görev | Öğrenci 1 | Öğrenci 2 | Ortak |
|---|---|---|---|
| Measurement audit / calibration |  |  |  |
| ns-3 kodu / config |  |  |  |
| Deney campaign |  |  |  |
| Data analysis / plotting |  |  |  |
| Rapor |  |  |  |
| Sunum / Q&A hazırlığı |  |  |  |

İki öğrenci de projenin tamamını temel düzeyde açıklayabilmelidir.

## I. AI / LLM kullanım planı

| Planlanan kullanım | Araç / amaç | Nasıl doğrulanacak? |
|---|---|---|
| Kod/API yardımı |  |  |
| Debugging |  |  |
| Analiz / plotting |  |  |
| Yazım / dil |  |  |
| Diğer |  |  |

Önemli kullanım private repo'daki `AI_USAGE.md` dosyasında ayrıca kaydedilir.

## J. Riskler ve ihtiyaç duyulan destek

- En büyük teknik risk:
- İhtiyaç duyulan yazılım / ortam / veri:
- Eğitmenden beklenen onay / yardım:

## K. Eğitmen onayı

- Atanan proje ID:
- Scope düzeltmesi:
- Core matrix değişikliği gerekiyorsa:
- Onay / tarih:
