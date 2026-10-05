# AI / LLM Kullanım Politikası

## Temel ilke

AI araçlarının kullanımı **serbesttir**, ancak önemli kullanım **açıklanmalı, doğrulanmalı ve öğrenci tarafından anlaşılmalıdır**. Proje notu, kodun hiçbir yardım almadan yazılmış olmasına değil; mühendislik muhakemesine, doğrulanabilir deneye ve reproducible kanıta dayanır.

## İzin verilen kullanım örnekleri

- ns-3 API'sini veya compiler error'ını açıklatmak;
- C++ / Python syntax önerisi almak;
- kodu refactor etmek;
- experiment design veya plotting yaklaşımı için fikir almak;
- dil/gramer düzenlemesi;
- dokümantasyonu anlamaya yardımcı olmak.

## İzin verilmeyen kullanım

- ölçüm, simulation run, figure, citation veya sayısal sonuç uydurmak;
- grubun açıklayamadığı/değiştiremediği kodu teslim etmek;
- başka bir grubun private code/data'sını AI aracı üzerinden kullanmak;
- çalıştırılmamış bir simülasyonu çalıştırılmış gibi göstermek;
- experiment design, coding, analysis veya validation üzerindeki önemli AI katkısını gizlemek.

## Zorunlu `AI_USAGE.md`

Projeyi maddi biçimde etkileyen AI kullanımı için şu bilgiler tutulmalıdır:

```text
Araç:
Tarih:
Amaç:
Etkilenen dosya / analiz:
AI ne önerdi?
Nasıl doğruladık?
İnsan tarafından yapılan değişiklik / karar:
```

Tam prompt transcript'i **istenmez**.

## Doğrulama sorumluluğu

Her sonuçtan öğrenciler sorumludur. Doğrulama; resmî dokümantasyon, compile/test, baseline comparison, simülasyonu yeniden çalıştırma, birim/boyut kontrolü veya bağımsız hesaplama ile yapılabilir.

## Sözlü savunma

Her iki grup üyesinden bir kod parçasını açıklaması, bir parametre değişikliğinin sonucunu tahmin etmesi, run configuration'ı canlı değiştirmesi veya bir figure'ın nasıl üretildiğini açıklaması istenebilir. Repo çalışıyor olsa bile öğrencinin teslim ettiği işi açıklayamaması bireysel notu düşürebilir.

## Yayın notu

Ders çıktıları daha sonra bir yayına katkı sağlarsa, araştırma sonucunu etkileyen AI kullanımı hedef konferans/derginin güncel politikasına uygun biçimde açıklanacaktır.
