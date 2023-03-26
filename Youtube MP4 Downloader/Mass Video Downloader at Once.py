import os
import sys
import yt_dlp
from concurrent.futures import ThreadPoolExecutor

CONFIG_FILE = "config.txt"

def get_ffmpeg_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_path = os.path.join(script_dir, "ffmpeg", "bin")
    
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            path = f.read().strip()
            if path:
                return path
    return default_path

def save_ffmpeg_path(path):
    with open(CONFIG_FILE, "w") as f:
        f.write(path)

def is_ffmpeg_valid(path):
    if os.path.isfile(os.path.join(path, "ffmpeg.exe")):
        return True
    return False

def set_ffmpeg_path():
    ffmpeg_path = get_ffmpeg_path()
    while not is_ffmpeg_valid(ffmpeg_path):
        ffmpeg_path = input(f"Enter the path to the folder containing 'ffmpeg.exe' (current: {ffmpeg_path}): ").strip()
        if not is_ffmpeg_valid(ffmpeg_path):
            print("Invalid path. 'ffmpeg.exe' not found. Please try again.")
        else:
            save_ffmpeg_path(ffmpeg_path)
    return ffmpeg_path

def download_video(yt_url, ffmpeg_path):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': os.path.join(os.path.dirname(os.path.abspath(__file__)), '%(title)s.%(ext)s'),
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
    ffmpeg_path = set_ffmpeg_path()

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
