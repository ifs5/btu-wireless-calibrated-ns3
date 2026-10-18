# Eğitmen — Minimum Starter ve Kabul Kapıları

Bu sayfa **öğrenci çözümü içermez**; yalnız eğitmenin hazır etmesi ve doğrulaması gereken asgari başlangıç koşullarını tanımlar.

## K0 · Güvenilir ortak altyapı

- [ ] `run_matrix.py --dry-run` hiçbir sonuç dosyasını silmiyor; mevcut sürümde tehlikeli silme davranışı var.
- [ ] Gerçek çalıştırmada overwrite/resume kararı açık; sonuçların sessizce silinmesi mümkün değil.
- [ ] Sentetik `calibrated-channel.json` ile gerçek core çalışma fail-closed engelleniyor; `class_calibration_v1` için sürüm/kaynak kaydı var.
- [ ] ns-3.48 üzerinde common C++ başarıyla derlendi ve P01 P0/P1 mini koşusu CSV üretti.
- [ ] Minimum mekanizma doğrulaması, sadece CSV şema doğrulamasıyla karıştırılmıyor.

## K1 · 12 ortak-starter proje

- [ ] İlgili parametre değiştiğinde **gerçek PHY/MAC/topology uygulaması** değişiyor; sadece sonuç etiketini değiştirmek yeterli değil.
- [ ] Öğrenciye kalacak per-STA, time-bin, ek metrik/analiz modüllerinin **hazır çözümü public kodda yok**.
- [ ] P07'de 8 m'den coverage radius iddiası çıkarılmıyor; P09'un çapraz bant n varsayımı açıklanıyor.
- [ ] P11'in data/control mode yapılandırması doğru; P13 iki standardı aynı anlamlı koşullarda karşılaştırıyor.
- [ ] P16 time-bin kayıtları ve P08 per-client konumsal kayıtlar teknik olarak mümkün; çözümleri öğrenciye bırakılıyor.

## K2 · Özel projeler — yalnız çalışır başlangıç

| Proje | Eğitmen verecek | Öğrenci yazacak |
|---|---|---|
| P03 | İki hidden STA→AP + trafik + RTS kapalı + ortak kanal | RTS ON/OFF, retry/drop ölçümü, güvenilir kanıt |
| P12 | İki AP + STA association + UDP + same channel | Same/separate channel plan, per-BSS sayaç |
| P14 | QoS-capable AP/STA + iki traffic flow | ToS→AC eşleme, BE load senaryosu, per-class metrik |
| P15 | HE AP→çoklu STA **downlink** UDP + OFDMA kapalı | MU scheduler ON/OFF, per-STA KPI, gerçek DL MU frame kanıtı |

Bunlar **henüz tamamlanmadı**. Eğitmen bu başlangıçları ns-3.48'de derleyip asgari bağlantı testi yapmadan öğrencilere 'çalışır starter' sunmaz. P15 resmî ns-3 Wi-Fi modelinde MU scheduler varsayılan olarak bağlı değildir; yalnız scheduler işaretini değiştirmek, gerçek DL OFDMA kullanıldığını kanıtlamaz.

## K3 · Bütün projeler için kabul yaklaşımı

1. Öğrenci ana kod geliştirmesini private repoda commit eder; eğitmen baseline ile farkı inceler.
2. Olumlu ve sınır/olumsuz sentetik test + en az bir gerçek ns-3 koşusu aranır.
3. Testler **belirli bir performans artışını değil** doğru ölçüm ve mekanizmayı sınar.
4. Fiziksel donanım satın alma veya kampüs AP'lerini yeniden yapılandırma zorunluluğu yoktur.
5. Öğrenci sözlü savunmada kodu, kendi kararını ve sonuçların sınırlılığını açıklar.
6. Aynı 100 puanlık rubrik ve frozen matrix korunur; bu sözleşmeler yeni not kalemi oluşturmaz.

## Bir sonraki yürütme adımı

K0 güvenlik düzeltmeleri → common ns-3.48 gerçek P01 smoke-test → specialized dört **minimum iskelet** → 16 proje için instructor feasibility kontrolü → öğrenci tag/release. Bu belge hiçbir kapıyı geçilmiş olarak işaretlemez.
