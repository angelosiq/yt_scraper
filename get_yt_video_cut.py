from moviepy import VideoFileClip
from settings import BASE_VIDEO_PATH
from base import get_youtube_video_in_mp4_highest_resolution


def get_yt_video_cut():
    downloaded_file = get_youtube_video_in_mp4_highest_resolution()
    start_time = input("Enter the start time: ")
    end_time = input("Enter the end time: ")

    try:
        video = VideoFileClip(downloaded_file)
        subclip = video.subclipped(start_time, end_time)
        output_filename = f"{BASE_VIDEO_PATH}/cut_clip_{start_time}s_to_{end_time}s.mp4"
        print(f"Cutting video from {start_time}s to {end_time}s...")
        subclip.write_videofile(output_filename, codec="libx264")
        print(f"Cut clip saved as '{output_filename}'")
        video.close()
    except Exception as e:
        print(f"An error occurred while cutting the video: {e}")


if __name__ == "__main__":
    get_yt_video_cut()
