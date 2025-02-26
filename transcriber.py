import whisper
import os

def transcribe_video(video_path: str, model_name: str = "base") -> str:
    """
    Transcribe a video file using OpenAI's Whisper
    Args:
        video_path: Path to the video file
        model_name: Whisper model to use (tiny, base, small, medium, large)
    Returns:
        The transcribed text
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    print(f"Loading Whisper model: {model_name}")
    model = whisper.load_model(model_name)
    
    print("Starting transcription...")
    result = model.transcribe(video_path)
    
    return result["text"]