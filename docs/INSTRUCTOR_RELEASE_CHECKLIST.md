# Eğitmen Release Kontrol Listesi

Öğrenci starter sürümünü yayınlamadan önce tamamlanmalıdır.

- [ ] Public GitHub repo oluşturuldu; `LICENSE` altında GPL-2.0 lisans metni mevcut.
- [ ] Course starter release tag'i oluşturuldu/donduruldu (öneri: `student-starter-v1.0`).
- [x] Matrix runner dosya koruması / demo-calibration guard için **12 mock ns-3 testi** geçti (gerçek ns-3 testleri yerine geçmez).
- [ ] Gerçek `class_calibration_v1.json` ve `calibration/APPROVED_CORE_CALIBRATION.json` SHA-256 kilidi yayınlandı.
- [ ] Ortak ortamın ns-3.48 olduğu doğrulandı.
- [ ] `ns3/btu-calibrated-wifi.cc` aynı ortamda compile edildi.
- [ ] P01 için en az bir P0 ve bir P1 case uçtan uca çalıştırıldı.
- [ ] Smoke-test CSV üzerinde `validate_results.py` ve `aggregate_results.py` çalıştırıldı.
- [ ] P03/P12/P14/P15 specialized starter'ları `ADVANCED_STARTERS.md` içindeki resmî ns-3.48 örneklerinden uyarlandı ve smoke-test edildi.
- [ ] Measurement CSV schema ve class calibration version donduruldu.
- [ ] Synthetic calibration JSON ancak veri audit'inden sonra gerçek sınıf kalibrasyonu ile değiştirildi.
- [ ] Her project matrix için core-run budget grading specification ile karşılaştırıldı.
- [ ] Öğrenci geliştirme repolarının grading bitene kadar private olacağı duyuruldu.
- [ ] Project Specification, Proposal Template ve AI Policy LMS/repo üzerinden dağıtıldı.

## Yayına dönük ek kontroller

- [ ] Heterojen sınıf ölçümlerinden ayrı bir controlled reference measurement campaign planlandı.
- [ ] Calibration'da kullanılmayan hold-out measurement point/session ayrıldı.
- [ ] Dersin exploratory sonuçlarından temsilî senaryolar seçildikten sonra publication rerun manifest donduruldu.
- [ ] Öğrenci notları ve kişisel öğrenme verileri teknik research dataset'in dışında tutuldu.
