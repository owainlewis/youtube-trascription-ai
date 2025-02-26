#!/usr/bin/env python3
import yt_dlp
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

def download_video(video_url: str) -> str:
    # Ensure the downloads directory exists
    download_dir = 'downloads'
    os.makedirs(download_dir, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'progress_hooks': [progress_hook],
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'  # Prefer MP4 format
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            video_path = os.path.join(download_dir, f"{info['title']}.{info['ext']}")
            return video_path
    except Exception as e:
        print(f"\nAn error occurred while downloading the video: {e}")
        return None