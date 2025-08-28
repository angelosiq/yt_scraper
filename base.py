from pytubefix import YouTube
from pytubefix.cli import on_progress
from settings import BASE_VIDEO_PATH


def get_youtube_video_in_mp4_highest_resolution(video_url=None):
    try:
        if not video_url:
            video_url = input("Enter the YouTube video URL: ")
        yt = YouTube(video_url, on_progress_callback=on_progress)
        print(yt.title)
        ys = yt.streams.get_highest_resolution()
        return ys.download(output_path=BASE_VIDEO_PATH)
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")
