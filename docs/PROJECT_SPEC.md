# Kablosuz Ağlar Dönem Projesi — 2026–2027

**Projenin ders notuna etkisi:** %30  
**Grup büyüklüğü:** 2 öğrenci  
**Hedef:** 16 grup / 16 araştırma sorusu  
**Final sunumu:** 14. hafta; en fazla 5 slayt; 5 dakika sunum + 2 dakika soru-cevap

## Projenin temel fikri

Bu çalışma bir literatür özeti değildir. Tüm gruplar aynı araştırma akışını izler:

`ÖLÇ -> KALİBRE ET -> DOĞRULA -> SİMÜLE ET -> ANALİZ ET -> AÇIKLA`

Week 2–3 laboratuvar ölçümleri propagation bilgisini sağlar. Her ölçüm birimi/grup için log-distance exponent hesaplanır; daha sonra sınıf düzeyinde robust calibration durumları oluşturulur.

## Ortak propagation durumları

- **P0 textbook:** `n = 2.0` — zorunlu
- **P1 calibrated:** sınıf median `n` — zorunlu
- **P2 optimistic:** sınıf Q1 `n` — seçilmiş sensitivity/bonus çalışmaları
- **P3 pessimistic:** sınıf Q3 `n` — seçilmiş sensitivity/bonus çalışmaları

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

Zor bir projeyi seçmek otomatik bonus sağlamaz. Core çalışma eksiksiz ve reproducible hale geldikten sonra yapılan gerçek bir **Advanced Extension** için **+0…5 proje puanı** verilebilir.

## Öğrenci geliştirme akışı

Instructor starter repository public'tir. Öğrenci geliştirme repoları grading süresince private tutulmalıdır. Değerlendirme sonrasında reproducible ve uygun çalışmalar, izin/kredi süreci gözetilerek research repository'ye aktarılabilir.

Ayrıntılı repo kullanımı: [`REPO_KULLANIMI.md`](REPO_KULLANIMI.md)

İlgili dosyalar:

- `projects/project_catalog.csv`
- `projects/Pxx/README.md`
- `docs/AI_POLICY.md`
- `docs/REPRODUCIBILITY.md`
- `docs/PROJECT_SCHEDULE.md`
