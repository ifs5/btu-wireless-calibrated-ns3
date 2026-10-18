# 16 Proje — Öğrenci Yazılım Katkısı ve Kabul Testleri

**Bu belge proje çözümleri değil, görev sınırlarını tanımlar.** Amaç, öğrencilerin hazır matrisi yalnız çalıştırmak yerine **anlamlı kod geliştirmesi, onu test etmesi ve sonuçlarını yorumlamasıdır**. Proje konusu/değişkenleri/seed-run sayıları eğitmen tarafından belirlenmiştir; öğrenciler yeniden deney tasarlamaz.

## Ortak iş bölümü

| Eğitmen | Öğrenci |
|---|---|
| Sağlam ns-3.48 temel AP/STA simülasyonu ve P0/P1 kalibrasyon protokolü | Projeye özgü eksik ölçüm, konfigürasyon, topology veya analiz kodu |
| Önceden tanımlı 16 matrix ve güvenli çalıştırma altyapısı | Kod değişikliğine ait otomatik kabul testi |
| P03/P12/P14/P15 için yalnız **minimum çalışan mekanizma iskeleti** | Mekanizmayı araştırma sorusuna bağlayan gerçek geliştirme |
| Genel CSV, tekrar ve ortam kuralları | Ham sonuç, tekrar üretilebilir analiz, grafik, sınırlılıklar ve sözlü savunma |

**Yeterli sayılmaz:** yalnız parametreleri değiştirmek, 20–80 simülasyonu çalıştırmak, hazır sonucu kopyalamak. **Zorunlu öğrenci kanıtı:** (1) anlamlı C++/Python değişikliği, (2) bir olumlu ve bir sınır/olumsuz durumu kapsayan test, (3) veriden üretilmiş proje grafiği ve teknik yorum. Satır sayısı ölçüt değildir.

**Hazırlık durumu:** Bunlar yazılım tasarım/kabul ölçütleridir. ns-3.48 compile/smoke-test ve `class_calibration_v1` henüz tamamlanmadı. P03/P12/P14/P15 özel iskeletler henüz public repoda yok. Bunları çalışır öğrenci starter'ı diye tanıtmayın.

## Projeler

| Kod | Zorluk | Core run | Öğrencinin temel katkısı |
|---|---|---:|---|
| [P01](../projects/P01/STUDENT_TASKS.md) | Standard | 50 | Her STA'nın kimlik ve throughput değerini CSV'ye yazan modülü geliştir |
| [P02](../projects/P02/STUDENT_TASKS.md) | Standard | 50 | Toplam offered load ile teslim edilen goodput'u ayrı hesapla |
| [P03](../projects/P03/STUDENT_TASKS.md) | Intermediate | 20 | RTS/CTS açık-kapalı anahtarını MAC ayarına bağla |
| [P04](../projects/P04/STUDENT_TASKS.md) | Standard | 50 | Payload byte/packet sayılarını ve offered/delivered byte oranını üreten ek sayaç/an |
| [P05](../projects/P05/STUDENT_TASKS.md) | Intermediate | 80 | Log-distance path-loss kestirim kodunu yaz |
| [P06](../projects/P06/STUDENT_TASKS.md) | Standard | 50 | Mesafe-KPI analiz modülü ve önceden seçilmiş PDR eşiğine göre en uzak deney noktası |
| [P07](../projects/P07/STUDENT_TASKS.md) | Standard | 50 | Bu **8 m koşulunda** önceden açıklanmış PDR hedefine ulaşan en düşük Tx power'ı bul |
| [P08](../projects/P08/STUDENT_TASKS.md) | Intermediate | 30 | STA ID–(x,y)–throughput/PDR kayıt kodu ile üç yerleşimin mekânsal performans harita |
| [P09](../projects/P09/STUDENT_TASKS.md) | Intermediate | 40 | Bant bazlı path-loss/parametre audit script'i ve aynı n varsayımında paired compari |
| [P10](../projects/P10/STUDENT_TASKS.md) | Intermediate | 30 | Mbps/MHz normalize edilmiş verimlilik analizi yaz |
| [P11](../projects/P11/STUDENT_TASKS.md) | Intermediate | 40 | Geçerli data/control mode ayrımını ns-3.48'e uygun kur |
| [P12](../projects/P12/STUDENT_TASKS.md) | Advanced | 20 | Same/separate channel planını uygula, gerçek BSSID/association kontrolü ekle, BSS b |
| [P13](../projects/P13/STUDENT_TASKS.md) | Intermediate | 40 | Uygulanan PHY/MAC ayarlarını raporlayan konfigürasyon audit aracı ve kontrollü stan |
| [P14](../projects/P14/STUDENT_TASKS.md) | Advanced | 20 | ToS/user priority→EDCA AC eşlemesini kodla |
| [P15](../projects/P15/STUDENT_TASKS.md) | Advanced | 20 | OFDMA ON/OFF için RrMultiUserScheduler bağlama mantığını kodla |
| [P16](../projects/P16/STUDENT_TASKS.md) | Intermediate | 30 | Sabit zaman aralığında STA pozisyonu ve teslim edilen byte sayacı |

**Toplam:** 16 konu, bütün 16 konu atanırsa 620 çekirdek koşu. 30 kişilik sınıfta 15 ikili grup 16 konudan 15'ini alır; 32 kişi olursa 16'sı atanabilir. **Notlandırma rubriği değiştirilmedi.**

## Ön koşullar ve sürüm

- Gerçek sınıf verisi `class_calibration_v1` yayımlanmadan demo JSON ile bilimsel sonuç üretilmez.
- P07 tek mesafe tarar: 'coverage radius' yerine 8 m hizmet eşiği karşılaştırılır.
- P15 için DL OFDMA'yı ölçmek **AP→STA downlink trafik ve gerçek MU frame kanıtı** gerektirir.
- Özel starter'lar tüm protokolü öğrencilerin sıfırdan yeniden yazması anlamına gelmez.
- Öğrencinin kodlaması gereken özellik **eğitmenin minimum iskeletinde hazır verilmemelidir**.
- Bu aşamada yeni öğrenci çözümü veya eğitmen reference implementation yazılmamıştır.
