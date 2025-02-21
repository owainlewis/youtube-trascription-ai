#!/usr/bin/env python3
import yt_dlp
import sys
import os

def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded = d.get('downloaded_bytes', 0)
        total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
        if total:
            percent = downloaded / total * 100
            print(f"Downloading: {percent:.1f}% complete", end='\r')
    elif d['status'] == 'finished':
        print("\nDownload complete, now post-processing...")

def download_video(video_url: str):
    # Ensure the downloads directory exists
    download_dir = 'downloads'
    os.makedirs(download_dir, exist_ok=True)

    # Set options for downloading video as MP4 with progress hooks.
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'progress_hooks': [progress_hook],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print(f"\nAn error occurred while downloading the video: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <video_url>")
        sys.exit(1)

    video_url = sys.argv[1]
    download_video(video_url)

if __name__ == '__main__':
    main()