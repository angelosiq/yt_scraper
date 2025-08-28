from pytubefix import YouTube
from pytubefix.cli import on_progress
from settings import BASE_AUDIO_PATH


def get_youtube_video_audio_only():
    try:
        video_url = input("Enter the YouTube video URL: ")
        yt = YouTube(video_url, on_progress_callback=on_progress)
        print(yt.title)
        ys = yt.streams.get_audio_only()
        ys.download(output_path=BASE_AUDIO_PATH)
    except Exception as e:
        print(f"An error occurred while downloading the audio: {e}")


if __name__ == "__main__":
    get_youtube_video_audio_only()
