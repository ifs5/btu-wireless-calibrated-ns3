# Ortam Kurulumu

Hedef simulator: **ns-3.48**. Ders kapsamında desteklenen ortak ortam Linux/Ubuntu'dur.

## Önerilen kurulum/doğrulama akışı

1. ns-3.48'i resmî ns-3 release/project source üzerinden edinin ve build edin.
2. Önce ns-3 build tree'yi doğrulayın ve resmî bir Wi-Fi örneğini çalıştırın.
3. Common-starter projeler için bu repodan önce `--dry-run` çalıştırın:

```bash
python3 scripts/run_matrix.py \
  --ns3-root /path/to/ns-3.48 \
  --matrix projects/P01/matrix.json \
  --dry-run
```

4. Matrix ve calibration dosyasını kontrol ettikten sonra `--dry-run` seçeneğini kaldırın.
5. P03/P12/P14/P15 specialized projeleri `docs/ADVANCED_STARTERS.md` akışını izler ve single-AP common engine yerine belirtilen resmî ns-3.48 örneğinden başlar.

## Reproducibility kuralı

Eğitmen onayı olmadan proje sırasında simulator sürümünü yükseltmeyin. Final repo'da exact ns-3 version, compiler/OS, calibration JSON hash, matrix file ve seed/run policy belgelenmelidir.
