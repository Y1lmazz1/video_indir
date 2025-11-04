from yt_dlp import YoutubeDL
import os
import subprocess

def download_video_only(url):
    options = {
        'outtmpl': '%(title)s_video.%(ext)s',
        'format': 'bestvideo',   # sadece video
        'noplaylist': True,
    }
    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info)
        print(f"🎬 Video indirildi: {os.path.abspath(video_file)}")
        return video_file

def download_audio_only(url):
    options = {
        'outtmpl': '%(title)s_audio.%(ext)s',
        'format': 'bestaudio',   # sadece ses
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
    }
    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        audio_file = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp3"
        print(f"🎵 Ses indirildi: {os.path.abspath(audio_file)}")
        return audio_file

def merge_video_audio(video_file, audio_file, output_file):
    command = [
        'ffmpeg',
        '-i', video_file,
        '-i', audio_file,
        '-c:v', 'copy',   
        '-c:a', 'aac',    
        '-strict', 'experimental',
        output_file
    ]
    subprocess.run(command, check=True)
    print(f"✅ Video ve ses birleştirildi: {os.path.abspath(output_file)}")

 
    if os.path.exists(video_file):
        os.remove(video_file)
    if os.path.exists(audio_file):
        os.remove(audio_file)
    print("🗑️ Geçici dosyalar silindi.")

if __name__ == "__main__":
    link = input("🎥 Video linkini yapıştırın: ")

    video_path = download_video_only(link)
    audio_path = download_audio_only(link)
    
    output_path = os.path.splitext(video_path)[0] + "_final.mp4"
    merge_video_audio(video_path, audio_path, output_path)

    input("Program tamamlandı. Çıkmak için Enter’a basın...")
