# BTÜ Ölçüm-Kalibrasyonlu Kablosuz Ağlar / ns-3 (2026–2027)

Bu depo, **Kablosuz Ağlar** dersi dönem projesi için ortak araştırma ve simülasyon altyapısıdır.

Temel yaklaşımımız:

`ÖLÇ -> KALİBRE ET -> DOĞRULA -> SİMÜLE ET -> ANALİZ ET -> AÇIKLA`

Tüm gruplar aynı ölçüm-temelli propagation baseline'ını, aynı seed/run politikasını ve ortak sonuç şemasını kullanır; fakat farklı network-level araştırma sorularını inceler. Böylece projeler ayrı olsa da dönem sonunda sonuçlar birleştirilebilir ve seçilen senaryolar yayın kalitesinde tekrar çalıştırılabilir.

## Hedef ortam

- **ns-3.48**
- Ortak ders ortamı için Linux/Ubuntu önerilir
- Orkestrasyon ve analiz için Python 3.10+
- Teknik değişken/alan adları (`project_id`, `n_sta`, `model_label` vb.) veri birleştirme ve yayın reproducibility'si için İngilizce tutulur; açıklamalar Türkçedir.

Resmî ns-3 dokümantasyonu: https://www.nsnam.org/docs/

## Hızlı başlangıç

### 1. ns-3.48'i kurun ve doğrulayın

Kurulum adımları için [`environment/SETUP.md`](environment/SETUP.md) dosyasını izleyin.

### 2. Week 2–3 ölçümlerinizi ortak şemaya aktarın

Şablon:

`calibration/raw/measurement_template.csv`

Sınıf ölçümlerinden calibration üretmek için:

```bash
python3 scripts/estimate_calibration.py calibration/raw/class_measurements.csv \
  --output-json calibration/outputs/calibrated-channel.json \
  --summary-csv calibration/outputs/calibration-units.csv
```

Bu adım her ölçüm birimi/grup için log-distance exponent `n` hesaplar; sınıf ortak kalibrasyonu için grup bazlı `n` değerlerinin median/Q1/Q3 özetini üretir.

### 3. Size atanan projeyi açın

Örneğin P01:

```text
projects/P01/
├── README.md
└── matrix.json
```

16 projenin özeti için [`docs/PROJECT_CATALOG.md`](docs/PROJECT_CATALOG.md) dosyasına bakın.

### 4. Önce dry-run yapın

```bash
python3 scripts/run_matrix.py \
  --ns3-root /path/to/ns-3.48 \
  --matrix projects/P01/matrix.json \
  --dry-run
```

Komutlar beklediğiniz gibiyse `--dry-run` seçeneğini kaldırarak deney matrisini çalıştırın.

### 5. Sonuçları doğrulayın ve özetleyin

```bash
python3 scripts/validate_results.py results/P01_raw.csv
python3 scripts/aggregate_results.py results/P01_raw.csv --output results/P01_summary.csv
```

## Ortak propagation durumları

- **P0 — Textbook:** `n = 2.0`
- **P1 — Calibrated:** sınıf median `n`
- **P2 — Optimistic:** sınıf Q1 `n` (çoğunlukla sensitivity/bonus)
- **P3 — Pessimistic:** sınıf Q3 `n` (çoğunlukla sensitivity/bonus)

Önemli modelleme kuralı: Week 3'te fit edilen RSSI intercept `A`, ns-3 `ReferenceLoss` ile aynı şey değildir. Core workflow'da `ReferenceLoss`, ilgili frekans için 1 m Friis loss olarak hesaplanır; ölçümden doğrudan aktardığımız temel parametre `n` değeridir.

## Starter kapsamı

Ortak `ns3/btu-calibrated-wifi.cc` motoru şu projelerin temel starter'ıdır:

**P01, P02, P04–P11, P13 ve P16.**

P03, P12, P14 ve P15; hidden terminal, iki BSS interference, EDCA ve OFDMA gibi mekanizmalar nedeniyle özel starter gerektirir. Bu projelerde resmî ns-3.48 örnekleri temel alınır. Ayrıntılar: [`docs/ADVANCED_STARTERS.md`](docs/ADVANCED_STARTERS.md).

## Repo nasıl kullanılacak?

Bu **public instructor repository** şunları içerir:

- ortak starter code,
- kalibrasyon araçları,
- proje matrisleri,
- ortak sonuç şeması,
- reproducibility kuralları,
- AI/LLM kullanım politikası,
- dönem sonunda anonimleştirilmiş/agregat research artifacts.

Öğrenci grupları geliştirmelerini **grading tamamlanana kadar private repository** üzerinde yapmalıdır. Public repodan starter sürümü alınır; öğrenci repo'sunda kendi kodu, `AI_USAGE.md`, raw results ve analysis dosyaları tutulur. Ayrıntılı akış: [`docs/REPO_KULLANIMI.md`](docs/REPO_KULLANIMI.md).

## Öğrenci belgeleri

- Proje şartnamesi: [`docs/PROJECT_SPEC.md`](docs/PROJECT_SPEC.md)
- Proposal şablonu: [`docs/PROPOSAL_TEMPLATE.md`](docs/PROPOSAL_TEMPLATE.md)
- AI/LLM politikası: [`docs/AI_POLICY.md`](docs/AI_POLICY.md)
- Repo kullanım kılavuzu: [`docs/REPO_KULLANIMI.md`](docs/REPO_KULLANIMI.md)

## AI / LLM kullanımı

AI araçları yasak değildir. İlke:

> **AI kullanımına izin verilir; önemli kullanım açıklanmalı, doğrulanmalı ve öğrenci tarafından anlaşılmalıdır.**

Her öğrenci reposunda `AI_USAGE.md` bulunmalıdır. Ayrıntılar: [`docs/AI_POLICY.md`](docs/AI_POLICY.md).

## Reproducibility

Aynı `matrix.json`, calibration dosyası, seed/run politikası ve commit ile sonuçların tekrar üretilebilir olması beklenir. Kurallar: [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md).

## Lisans

ns-3 ile bağlantılı starter C++ kodu `GPL-2.0-only` uyumluluğu gözetilerek hazırlanmıştır. Depoda GNU GPL v2 lisans metni `LICENSE` altında yer alır.

## Eğitmen için release notu

Öğrencilere dağıtmadan önce common starter ve özel starter'lar aynı ns-3.48 ortamında compile/smoke-test edilmelidir. Kontrol listesi: [`docs/INSTRUCTOR_RELEASE_CHECKLIST.md`](docs/INSTRUCTOR_RELEASE_CHECKLIST.md).
