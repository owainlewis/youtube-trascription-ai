# Open AI
import whisper
# YouTube 
import yt_dlp

import sys

class VideoDownloader():

    def __init__(self):
        self.default_opts = {
            'verbose': False,
            'format_sort': ['res:720', 'ext:mp4:m4a']
        }

    def download(self, video_url: str):
        with yt_dlp.YoutubeDL(self.default_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            output_filename = ydl.prepare_filename(info_dict)
            return output_filename

class VideoTranscriber():    

    def __init__(self, model="base"):
        self.model = model

    def mp4_to_text(self, file_path: str): 
        model = whisper.load_model(self.model)
        result = model.transcribe(file_path)
        return result["text"]


def main(): 
    file_name = sys.argv[1]

    downloader = VideoDownloader()

    transcriber = VideoTranscriber()

    file_name = downloader.download(file_name)

    transcript = transcriber.mp4_to_text(file_name)

    print(transcript)
    
    with open('transcript.txt', 'w') as f:
        f.write(transcript)
        
if __name__ == '__main__':
    main()    
