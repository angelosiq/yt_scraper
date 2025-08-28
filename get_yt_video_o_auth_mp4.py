from pytubefix import YouTube
from pytubefix.cli import on_progress
from settings import BASE_VIDEO_PATH


def get_youtube_video_in_mp4_highest_resolution_with_o_auth():
    try:
        video_url = input("Enter the YouTube video URL: ")
        yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=BASE_VIDEO_PATH)
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")


if __name__ == "__main__":
    get_youtube_video_in_mp4_highest_resolution_with_o_auth()
