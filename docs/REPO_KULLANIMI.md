# Repo Kullanım Kılavuzu

Bu doküman public instructor repo ile öğrenci grubunun private development repo'sunun nasıl birlikte kullanılacağını açıklar.

## 1. Public repo'nun rolü

Bu repo **tek doğruluk kaynağıdır (authoritative starter source)**:

- ortak ns-3 starter code,
- calibration scripts,
- proje katalog/matrisleri,
- ortak result schema,
- AI ve reproducibility kuralları,
- eğitmen tarafından yayınlanan düzeltmeler.

Öğrenciler public repo'ya doğrudan geliştirme commit'i göndermemelidir.

## 2. Öğrenci private repo'su

Her 2 kişilik grup bir private repo kullanır. Önerilen yapı:

```text
Pxx-team-name/
├── README.md
├── AI_USAGE.md
├── upstream/
│   └── starter-version.txt
├── code/
├── config/
├── data/
│   ├── raw/
│   └── processed/
├── results/
│   ├── raw/
│   └── summary/
├── analysis/
└── figures/
```

## 3. Starter sürümünü kaydedin

Çalışmaya başlamadan önce public repo'nun commit SHA/tag bilgisini private repo'nuzda kaydedin. Örneğin:

```text
starter tag: project-v0.1
starter commit: <SHA>
ns-3: 3.48
```

Final raporda kullanılan starter sürümü belirtilmelidir.

## 4. Kendi projenizi bulun

`projects/Pxx/README.md` araştırma sorusunu; `projects/Pxx/matrix.json` ise frozen core experiment matrix'i tanımlar.

Core matrix üzerinde değişiklik yapmak gerekiyorsa önce eğitmen onayı alın. Exploratory/bonus run'ları ayrı etiketleyin.

## 5. Calibration dosyasını değiştirmeyin

Sınıf için yayınlanan `calibration/outputs/calibrated-channel.json` ortak girdidir. Grup kendi istediği `n` değerini P1 olarak kullanmamalıdır. Farklı `n` denemeleri P2/P3 sensitivity veya açıkça etiketli exploratory run olmalıdır.

## 6. Tipik komut akışı

```bash
# 1) Matrix'i incele
python3 scripts/run_matrix.py \
  --ns3-root /path/to/ns-3.48 \
  --matrix projects/P01/matrix.json \
  --dry-run

# 2) Core run'ları çalıştır
python3 scripts/run_matrix.py \
  --ns3-root /path/to/ns-3.48 \
  --matrix projects/P01/matrix.json

# 3) Raw sonucu doğrula
python3 scripts/validate_results.py results/P01_raw.csv

# 4) Tekrarları özetle
python3 scripts/aggregate_results.py results/P01_raw.csv \
  --output results/P01_summary.csv
```

## 7. Commit ve evidence

- Tek bir final commit yerine proje boyunca düzenli, anlamlı commit'ler yapın.
- Commit sayısı not değildir; history yalnız development evidence olarak kullanılır.
- Raw CSV dosyalarını sonradan elle değiştirmeyin.
- Figure üretme script/notebook'unu saklayın.
- Her önemli AI kullanımını `AI_USAGE.md` içinde kaydedin.

## 8. Upstream düzeltmeleri

Eğitmen public repo'da hata düzeltmesi yayınlarsa duyurulan tag/commit'i dikkate alın. Kendi private repo'nuzdaki kodla kontrollü biçimde karşılaştırın; sonuçları etkileyen değişiklikleri raporda belirtin.

## 9. Final teslimde beklenen reproducibility bilgisi

Final repo en az şunları açıkça belirtmelidir:

- project ID,
- starter tag/commit,
- ns-3 version,
- calibration file/version,
- seed/run policy,
- core matrix,
- sonuçları üretme komutları,
- figure'ları üretme komutları,
- AI kullanım beyanı.
