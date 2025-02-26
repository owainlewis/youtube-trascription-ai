#!/usr/bin/env python3
import sys
from downloader import download_video
from transcriber import transcribe_video

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <video_url> [--download-only] [whisper_model]")
        print("Available whisper models: tiny, base, small, medium, large")
        sys.exit(1)

    video_url = sys.argv[1]
    download_only = "--download-only" in sys.argv
    
    # Remove --download-only from args if present to not interfere with model name
    args = [arg for arg in sys.argv if arg != "--download-only"]
    model_name = args[2] if len(args) > 2 else "base"

    # Download the video
    video_path = download_video(video_url)
    if not video_path:
        sys.exit(1)
    
    if download_only:
        print(f"\nVideo downloaded successfully to: {video_path}")
        return

    # Transcribe the video
    try:
        transcription = transcribe_video(video_path, model_name)
        print("\nTranscription:")
        print("-" * 80)
        print(transcription)
        print("-" * 80)
    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
