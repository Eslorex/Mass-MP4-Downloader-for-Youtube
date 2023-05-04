import os
import sys
import yt_dlp

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_ffmpeg_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_path = os.path.join(script_dir, "ffmpeg", "bin")
    
    return default_path

def set_ffmpeg_path():
    ffmpeg_path = get_ffmpeg_path()
    return ffmpeg_path

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

        for url in yt_urls:
            download_video(url, ffmpeg_path)

if __name__ == "__main__":
    main()
