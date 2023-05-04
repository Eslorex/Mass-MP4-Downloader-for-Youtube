import os
import sys
import yt_dlp
from concurrent.futures import ThreadPoolExecutor

def get_ffmpeg_path():
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, "ffmpeg", "bin")

def download_video(yt_url, ffmpeg_path):
    try:
        output_path = os.path.join(os.getcwd(), "Videos")
        os.makedirs(output_path, exist_ok=True)

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'merge_output_format': 'mp4',
            'postprocessors': [
                {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'},
            ],
            'ffmpeg_location': os.path.join(ffmpeg_path, ''),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(yt_url, download=False)
            print(f"Downloading: {info_dict['title']}")
            ydl.download([yt_url])

        print(f"Downloaded: {info_dict['title']}\n")
    except Exception as e:
        print(f"Error: {e}")




def main():
    ffmpeg_path = get_ffmpeg_path()

    while True:
        print("Enter YouTube video URLs, one per line. Press Enter twice to start downloading.")
        yt_urls = []
        while True:
            yt_url = input().strip()
            if yt_url:
                yt_urls.append(yt_url)
            else:
                break

        with ThreadPoolExecutor() as executor:
            executor.map(lambda url: download_video(url, ffmpeg_path), yt_urls)

if __name__ == "__main__":
    main()
