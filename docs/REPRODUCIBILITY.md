# Reproducibility Kuralları

1. Course repository'de belirtilen frozen ns-3 release kullanılmalıdır (ilk hedef: **ns-3.48**).
2. Raw measurements ve raw simulation CSV dosyaları korunmalıdır.
3. Ortak class calibration JSON kullanılmalı; `n` değeri sessizce “daha güzel sonuç veren” bir değerle değiştirilmemelidir.
4. Ders tarafından verilen sabit RNG seed ve tekrarlar için bağımsız ns-3 run numaraları kullanılmalıdır.
5. Project matrix aksi belirtmedikçe core experiments beş bağımsız run numarası kullanır.
6. Sonucu “uygunsuz” olduğu için run silinmez. Gerçek simulation failure ayrı ve belgeli olarak işaretlenir.
7. Code + matrix configuration + result CSV + analysis/plotting komutları finaldeki her figure'ı yeniden üretmek için yeterli olmalıdır.
8. Software version, commit hash, project ID, scenario ID, propagation model label, seed ve run kaydedilmelidir.
9. Exploratory/bonus run'lar frozen core dataset ile etiketsiz biçimde karıştırılmamalıdır.
10. Ders sonrasında publication-quality rerun yapılırsa frozen experiment manifest ve ayrı output directory kullanılır.
