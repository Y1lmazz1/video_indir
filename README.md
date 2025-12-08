Bu depo, yt-dlp ve FFmpeg kütüphanelerini kullanarak bir YouTube videosundan en iyi video ve ses akışlarını indirip bunları otomatik olarak tek bir çıktı dosyasında birleştiren bir Python betiği içerir.

 
✨ Temel Özellikler
Ayrı İndirme: Yüksek kaliteli video ve ses akışlarını bağımsız olarak çeker.

Otomatik Birleştirme: FFmpeg aracılığıyla indirilen parçaları tek bir nihai dosyada birleştirir.

Temizlik: İşlem tamamlandığında geçici video ve ses dosyalarını otomatik olarak siler.

Esneklik: Kullanıcıdan sadece URL girişi bekler.

🚀 Kurulum
Betiği çalıştırmadan önce gerekli araçları kurmanız gerekmektedir:

1. Python Bağımlılıkları
yt-dlp kütüphanesini yükleyin:

Bash

pip install yt-dlp
2. FFmpeg
FFmpeg'in sisteminizde kurulu olduğundan ve PATH'inizde erişilebilir olduğundan emin olun.

💡 Kullanım
video_indir.py dosyasını kaydedin.

Terminali açın ve betiği çalıştırın:
İstenen YouTube URL'sini yapıştırın:
<img width="1097" height="207" alt="Ekran görüntüsü 2025-11-04 125440" src="https://github.com/user-attachments/assets/9ae38509-06e6-405a-a785-dd54e2ff439e" />


Betiğin bitmesini bekleyin. Sonuç dosyası, orijinal dosya adı üzerine _final.mp4 eklenerek kaydedilecektir.<img width="1088" height="480" alt="Ekran görüntüsü 2025-11-04 125638" src="https://github.com/user-attachments/assets/b0d3e4dd-da7b-4043-ab92-8acd49658401" />
