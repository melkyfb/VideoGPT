import youtube_dl
import requests

def retrieve_video_url(video_url):
    # Retrieve the video URL using youtube_dl library
    ydl_opts = {
        "quiet": True,
        "format": "best[ext=mp4]/best[ext=avi]/best",
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        video_url = info['url']

    return video_url

def download_video(video_url):
    # Download the video using requests library
    response = requests.get(video_url)
    video_path = "video.mp4"  # Set the path where the video will be saved
    with open(video_path, "wb") as file:
        file.write(response.content)

    return video_path
