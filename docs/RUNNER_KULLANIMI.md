# Güvenli ns-3 deney çalıştırıcısı — kullanım ve onay süreci

Bu belge **eğitmen tarafından sağlanan otomasyonun** nasıl kullanılacağını açıklar. Öğrencinin kendisine ait kod geliştirme, kabul testleri, analiz ve yorum yapma sorumluluğunu ortadan kaldırmaz.

## A. Şu anda güvenle yapılabilecek işlem: dry-run

```bash
python3 scripts/run_matrix.py \
  --ns3-root /path/to/ns-3.48 \
  --matrix projects/P01/matrix.json \
  --dry-run
```

Bu işlem yalnızca 50 simülasyon komutunu **listeler**. ns-3'ü derlemez/çalıştırmaz; sonuç klasörü, CSV veya scratch dosyası oluşturmaz, mevcut dosyaları silmez. Mevcut sentetik JSON sayıları yalnızca örnek komut oluşturmak için kullanılır; bunlardan bilimsel sonuç çıkarılmaz.

**P03/P12/P14/P15** özel starter gerektirdiğinden bu ortak script onları bilerek çalıştırmaz.

## B. Neden gerçek koşu bugün otomatik başlamıyor?

Önce eski altı beş kişilik laboratuvar grubunun LOS RSSI–mesafe ham verileri eğitmen tarafından incelenir. En az dört geçerli bağımsız set varsa her biri için n hesaplanır ve sınıf medyan/Q1/Q3 değerleri alınır; değilse dokümandaki standart yeniden ölçüm yapılır.

Eğitmen şu iki dosyayı yalnızca audit sonrasında yayımlar:

1. `calibration/outputs/class_calibration_v1.json` — gerçek ölçümden hesaplanan sınıf n değerleri.
2. `calibration/APPROVED_CORE_CALIBRATION.json` — gerçek JSON dosyasının kilitlenmiş SHA-256 özeti.

**Şu anda repoda ikisi de yoktur. Bu kasıtlıdır; demo dosya ile gerçek deney yapılmasını önler.**

Gerçek sınıf JSON'unda eski alanlara ek olarak şu bilgiler bulunur:

```json
{
  "calibration_id": "class_calibration_v1",
  "data_origin": "measured_los",
  "band_ghz": 5.0,
  "unit_count": 6,
  "n_textbook": 2.0,
  "n_median": 2.2,
  "n_q1": 1.95,
  "n_q3": 2.45,
  "reference_loss_db": 46.427183
}
```

**DİKKAT: Bu değerler yalnız şema örneğidir; gerçek sınıf verisi değildir.** `unit_count` kabul edilen gerçek eski laboratuvar grubu sayısıdır; en az dört olmalıdır. Diğer alanlar `estimate_calibration.py` ile elde edilen gerçek çıktılardan korunur.

Eğitmen bu **gerçek dosya** için örneğin macOS'ta `shasum -a 256 calibration/outputs/class_calibration_v1.json` veya Linux'ta `sha256sum ...` ile hash hesaplar ve aşağıdaki biçimde onay kaydı yayımlar:

```json
{
  "status": "approved",
  "calibration_id": "class_calibration_v1",
  "sha256": "BURAYA_64_HANELI_GERCEK_SHA256"
}
```

Bu kilit yalnız **kazara yanlış dosya kullanılmasını önleyen bütünlük kontrolüdür**, dijital imza veya verinin bilimsel doğruluğu için otomatik kanıt değildir. Audit, kabul/ret gerekçeleri ve ders kalibrasyonu eğitmen sorumluluğundadır. Öğrenciler kendileri onay dosyası üretmemelidir.

## C. Onaylı starter release sonrasında gerçek çalışma

Öğrenci kendi private geliştirme reposunda uygun değişikliklerini ve proje testlerini tamamladıktan sonra:

```bash
python3 scripts/run_matrix.py \
  --ns3-root /path/to/ns-3.48 \
  --matrix projects/P01/matrix.json \
  --calibration calibration/outputs/class_calibration_v1.json
```

- **Ön kontrol:** Matrisin kimlikleri, placeholder'ları, kalibrasyon içeriği ve SHA-256 kilidi incelenir.
- **Kaynak koruma:** ns-3 `scratch/btu-calibrated-wifi.cc` içinde farklı içerikli dosya varsa otomatik üzerine yazılmaz.
- **Çıktı koruma:** `results/P01_raw.csv` veya manifest zaten varsa çalışma başlamadan reddedilir.
- **Tam çalışma:** Runner ayrı ve gizli bir `.pending.csv` dosyasına yazar; bütün beklenen run kimlikleri tamamlanmadan final CSV oluşturulmaz/değişmez.
- **Başarı:** `results/P01_raw.csv` yanında `results/P01_raw.csv.manifest.json` oluşur. Manifest; kullanılan matris, kalibrasyon, starter ve çıktı SHA-256 değerlerini içerir.
- **Hata:** Mevcut final CSV korunur. Kısmi `.pending.csv` dosyası inceleme için bırakılır; tam bilimsel sonuç sayılmaz.

Yeni bir tam koşuyla mevcut final sonuç dosyasını değiştirmek **bilinçli olarak** istenirse `--overwrite` kullanılır. Son koşunun eksik run'larından devam etme (`--resume`) **henüz desteklenmiyor**; eksikmiş gibi gösterilen sonuçlar otomatik birleştirilmez.

## D. Öğrencinin teslimi ve sonuçların korunması

- Matris dosyasını, onaylı kalibrasyon sürümünü, commit bilgisini ve manifest'i kaydedin.
- Raw CSV'yi **elle değiştirmeyin**; grafikler için ayrı analysis script'leri yazın.
- Public repo'nun `.gitignore` dosyası `results/*.csv` dosyalarını varsayılan olarak yoksayar. Private grup deposunda gerekiyorsa `git add -f results/P01_raw.csv` ile **bilinçli** ekleyin veya özel bir `data/raw/` dizininde uygun gizlilikle saklayın. Öğrenciye/kişiye ait veri public repoya gönderilmez.
- `validate_results.py` temel CSV biçim kontrolü sağlar; **PHY/MAC modelinin fiziksel doğruluğu için yeterli değildir**. Projeye özgü mekanizma kabul testleri ayrıca gerekir.

## E. Test komutu ve sınırlılık

```bash
python3 -m unittest discover -s tests -v
```

**12 güvenlik testi**, simülasyonu taklit eden küçük bir `fake ns3` uygulamasıyla yerelde geçmiştir. Gerçek ns-3.48 C++ compile/P01 uçtan uca smoke-test **ayrı ve henüz geçilmemiş** kontrol kapısıdır. Bu nedenle öğrenci release'i ilan edilmemiştir.
