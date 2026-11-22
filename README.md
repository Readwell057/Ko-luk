# Koçluk Takibi

Koç için öğrenci takip uygulaması: haftalık program, görevler, puan, sıralama ve PDF raporlar.

## Yükleme
1. Zip'i bilgisayarda/tablette aç, içindeki dosyaların hepsini GitHub'da yeni bir repoya yükle (Add file > Upload files).
2. Settings > Pages > Branch: main / (root) > Save. Birkaç dakika sonra uygulama linki hazır olur.
3. Tablette linki Chrome'da aç > menü > "Ana ekrana ekle". PDF paylaşma bu yolda çalışır.

## APK (isteğe bağlı)
1. Repoda Add file > Create new file. Adı kutusuna `.github/workflows/apk.yml` yaz, bu repodaki `apk.yml` dosyasının içeriğini yapıştır, commit et.
   (Zip'te `.github` klasörü de var; klasörü olduğu gibi yükleyebiliyorsan bu adıma gerek yok.)
2. Actions > APK > Run workflow. 3-5 dk sonra "kocluk-takibi-apk" çıktısını indir (zip içinde app-debug.apk).
3. APK'yı tablete at, "bilinmeyen kaynaklardan yükle" izni ver.

Not: Veriler cihazda saklanır. Ayarlar'dan düzenli yedek indir.
