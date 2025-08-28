from pytubefix import YouTube


def get_youtube_video_captions():
    try:
        video_url = input("Enter the YouTube video URL: ")
        yt = YouTube(video_url)
        print(yt.captions)
        caption = yt.captions['en']
        print(caption.generate_srt_captions())
    except Exception as e:
        print(f"An error occurred while getting the captions: {e}")


if __name__ == "__main__":
    get_youtube_video_captions()
