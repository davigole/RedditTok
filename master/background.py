import os
from moviepy.editor import VideoFileClip
from yt_dlp import YoutubeDL

from .console import create_log

BACKGROUND_SAMPLE = 'https://www.youtube.com/watch?v=GTaXbH6iSFA'

# Load background video and crop it to 9:16 aspect ratio
def load_background(path: str) -> VideoFileClip:
    video = VideoFileClip(path)
    
    width = 9/16 * video.h
    x1 = video.w/2 - width/2
    x2 = x1 + width

    return video.crop(x1=x1, x2=x2, y1=0, y2=video.h)

# Crop a portion of a video from start to end
def crop_video(video: VideoFileClip, start: int, end: int) -> VideoFileClip:
    return video.subclip(start, end)

# Remove audio from video
def remove_audio(video: VideoFileClip) -> VideoFileClip:
    return video.without_audio()

# Download sample background video - "Minecraft Relaxing Parkour 34 minutes 50 (lofi, no ads)" by SiswiZz
def download_sample() -> None:
    path = '../assets/background'
    log = create_log()

    if os.path.exists(path + '.mp4'):
        i = 1
        while os.path.exists('{} ({}).mp4'.format(path, i)): i += 1
        path = '{} ({}).mp4'.format(path, i)
    else:
        path += '.mp4'

    log.info('Downloading sample background video at {}. This may take a while'.format(path))

    ydl_opts = {
        'outtmpl': path,
        'merge_output_format': 'mp4'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(BACKGROUND_SAMPLE)

if __name__ == '__main__':
    download_sample()