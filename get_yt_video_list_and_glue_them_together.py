import os
from moviepy import VideoFileClip, concatenate_videoclips
from base import get_youtube_video_in_mp4_highest_resolution
from settings import BASE_VIDEO_PATH


def cut_and_concatenate(video_data, output_filename=f"{BASE_VIDEO_PATH}/combined_cut_video.mp4"):
    """
    Cuts specified segments from multiple videos and concatenates them.
    
    Args:
        video_data (list of dict): A list where each dictionary contains
                                   'url', 'start_time', and 'end_time'.
        output_filename (str): The name of the final output file.
    """
    final_clips = []
    downloaded_paths = []
    try:
        for data in video_data:
            path = get_youtube_video_in_mp4_highest_resolution(data['url'])
            if not path:
                continue
            downloaded_paths.append(path)
            video = VideoFileClip(path)
            subclip = video.subclipped(data['start_time'], data['end_time'])
            print(f"Adding a cut from {data['start_time']}s to {data['end_time']}s.")
            final_clips.append(subclip)
        if not final_clips:
            print("No video clips were created.")
            return
        print("Concatenating the video segments...")
        final_video = concatenate_videoclips(final_clips)
        final_video.write_videofile(output_filename, codec="libx264")
        print(f"Combined video saved as '{output_filename}'")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        for path in downloaded_paths:
            if os.path.exists(path):
                os.remove(path)
                print(f"Removed temporary file: {path}")


video_data_list = [
    {
        'url': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'start_time': 10,
        'end_time': 20
    },
    {
        'url': "https://www.youtube.com/watch?v=ndwPSA_WmAk",
        'start_time': 10,
        'end_time': 20
    }
]

cut_and_concatenate(video_data_list)
