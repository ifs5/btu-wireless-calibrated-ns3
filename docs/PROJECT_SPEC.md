# Kablosuz Ağlar Dönem Projesi — 2026–2027

**Projenin ders notuna etkisi:** %30  
**Grup büyüklüğü:** 2 öğrenci  
**Hedef:** 30 öğrenci için 15 ikili grup / 16 proje konusundan 15'i; kayıt 32 olursa 16 ikili grup  
**Final sunumu:** 14. hafta; en fazla 5 slayt; 5 dakika sunum + 2 dakika soru-cevap

## Projenin temel fikri

Bu çalışma bir literatür özeti değildir. Tüm gruplar aynı araştırma akışını izler:

`ÖLÇ -> KALİBRE ET -> DOĞRULA -> SİMÜLE ET -> ANALİZ ET -> AÇIKLA`

Kalibrasyonun öncelikli kaynağı **3. hafta LOS RSSI-mesafe ölçümleridir**. **Eski beş kişilik 6 laboratuvar grubu (L01–L06)** altı ölçüm birimidir; yeni ikili proje grupları bu sayıyı artırmaz.

### Kalibrasyon karar süreci

1. 5. haftada L01–L06 ham dosyaları toplanır. dBm, en az üç farklı mesafe ve her mesafede en az üç tekrar, aynı AP/BSSID, aynı band, karşılaştırılabilir LOS rota ve izlenebilir cihaz/oturum şartları kontrol edilir.
2. En az dört eski grup seti geçerliyse **her lab grubu için tek n** hesaplanır ve geçerli grup n değerleri birleştirilir. Geçerli grup sayısı dörtten azsa L01–L06 ekipleri 5. haftada aynı 5 GHz AP, rota, cihaz ve yöntemle 1/2/4/8/12 m ve üçer tekrardan oluşan yeni ortak ölçüm yapar. İki kampanya gelişigüzel karıştırılmaz.
3. Her grubun LOS fit eğimi `m` için `n=-m/10`. Sınıf P1 = geçerli grup n medyanı; P2=Q1 ve P3=Q3 (`QUARTILE.INC`).
4. Eğitmen 6. haftada `class_calibration_v1` sürümünü kaynak/ret gerekçeleriyle birlikte açıklar. Public repodaki mevcut `calibrated-channel.json` **sentetik örnektir, gerçek sınıf kalibrasyonu değildir**.

**Sayısal örnek (gerçek ölçüm değildir):** `n=[1.60, 1.90, 2.10, 2.30, 2.50, 2.90]` → P0=2; P1 medyan=2.20; P2 Q1=1.95; P3 Q3=2.45. P2 ve P3 ayrı medyanlar değil, alt/üst çeyreklerdir.

**Önemli P09 uyarısı:** 5 GHz'de elde edilen `n` değerini 2.4 GHz'e aktarmak yalnız kontrollü varsayımdır; 2.4 GHz için ölçüm-temelli kalibrasyon iddiasında bulunulmaz.

## Ortak propagation durumları

- **P0 textbook:** `n = 2.0` — zorunlu
- **P1 calibrated:** sınıf median `n` — zorunlu
- **P2 optimistic:** sınıf Q1 `n` — **P05 için zorunlu**, diğer projelerde sensitivity/bonus
- **P3 pessimistic:** sınıf Q3 `n` — **P05 için zorunlu**, diğer projelerde sensitivity/bonus

**Önemli:** Fit edilen RSSI intercept değeri ns-3 `ReferenceLoss` olarak doğrudan kullanılmaz. Core workflow, frekans ile uyumlu 1 m Friis loss değerini reference loss olarak kullanır; ölçümden `n` aktarılır.

## Tüm projeler için zorunlu bilimsel gereksinimler

Her proje aşağıdakileri içermelidir:

1. Açık bir research question ve test edilebilir hypothesis.
2. Birincil independent variable ve açıkça tanımlanmış controlled variables.
3. P0 vs P1 propagation karşılaştırması.
4. Dondurulmuş (frozen) scenario matrix ve dersin seed/run politikası.
5. Ham (raw) CSV sonuçları.
6. Tekrar koşularından mean, standard deviation ve %95 confidence interval.
7. Bir primary KPI ve proje ile ilişkili ortak metric'ler.
8. Kanıta dayalı interpretation ve limitations.
9. Reproducible repo yapısı.
10. `AI_USAGE.md` açıklama/doğrulama kaydı.

## Zorluk ve adalet

Zorluk **otomatik puanla değil, core scope ile** dengelenir. Standard projelerin deney matrisi daha geniştir. Advanced projelerin core matrisi daha küçüktür ve daha güçlü starter desteği vardır.

Zor bir projeyi seçmek otomatik bonus sağlamaz. Core çalışma eksiksiz ve reproducible hale geldikten sonra yapılan gerçek bir **Advanced Extension** için **+0…5 proje puanı** verilebilir. Bonus, proje bileşeninin ders başarı notuna katkısını **30 puanın üzerine çıkarmaz**. Final proje notu = min(100, core puanı + kazanılan bonus); ders katkısı = final proje notu × 0.30.

## Notlandırma

Proje 100 puan üzerinden değerlendirilir ve ders notuna %30 ağırlıkla yansıtılır.

| Bileşen | Puan |
|---|---:|
| Proposal ve araştırma sorusunun netliği | 5 |
| Ölçüm kaynağı, kalibrasyon ve P0/P1 baseline | 10 |
| Deney tasarımı, değişkenler ve frozen matrix | 15 |
| Teknik ns-3 uygulaması | 20 |
| Sonuçlar, istatistik ve kanıta dayalı yorum | 20 |
| Repo, ham veri, yeniden üretilebilirlik ve AI kaydı | 10 |
| Final rapor | 10 |
| Sunum ve bireysel soru-cevap | 10 |
| **TOPLAM** | **100** |

## Öğrenci geliştirme akışı

Instructor starter repository public'tir. Öğrenci geliştirme repoları grading süresince private tutulmalıdır. Değerlendirme sonrasında reproducible ve uygun çalışmalar, izin/kredi süreci gözetilerek research repository'ye aktarılabilir.

Ayrıntılı repo kullanımı: [`REPO_KULLANIMI.md`](REPO_KULLANIMI.md)

## Öğrenci belgeleri ve ilgili dosyalar

- [`PROPOSAL_TEMPLATE.md`](PROPOSAL_TEMPLATE.md)
- [`AI_POLICY.md`](AI_POLICY.md)
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md)
- [`PROJECT_SCHEDULE.md`](PROJECT_SCHEDULE.md)
- [`PROJECT_CATALOG.md`](PROJECT_CATALOG.md)
- `projects/project_catalog.csv`
- `projects/Pxx/README.md`

## Starter teslim koşulu

Mevcut `calibration/outputs/calibrated-channel.json` bir DEMO'dur. Öğrenciler, gerçek `class_calibration_v1` ve öğretmen tarafından test edilmiş ns-3.48 release açıklanmadan full core run başlatmamalıdır. P03/P12/P14/P15 ayrıca özel starter gerektirir.

## 16 konunun açıklaması

Her projenin araştırma sorusu, değişkenleri, core deneyleri ve sınırları [proje kataloğunda](PROJECT_CATALOG.md) ve `projects/Pxx/README.md` altında bulunur. Öğrencilere ayrıca *Kablosuz_Aglar_Donem_Projesi_Sartnamesi_Aciklamali_v2.docx* ve *Kablosuz_Aglar_Proje_Matrisi_Aciklamali_v2.xlsx* dağıtılır.
