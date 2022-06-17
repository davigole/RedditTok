from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, CompositeAudioClip, CompositeVideoClip

# Add audio to video
def add_audio(video: VideoFileClip, audio: AudioFileClip) -> VideoFileClip:
    video.audio = CompositeAudioClip([audio])
    return video


# Add title and comments screenshots over background video
def add_data(video: VideoFileClip, data: list) -> CompositeVideoClip:
    last = 0
    delay = AudioFileClip('assets/silence.mp3').duration

    for d in data:
        audio = AudioFileClip(d["audio"])
        screenshot = (ImageClip(d["screenshot"])
            .set_start(last)
            .set_end(last + audio.duration)
            .set_position("center", "center"))

        screenshot = screenshot.resize(video.w/screenshot.w)

        video = CompositeVideoClip([video, screenshot])

        last += delay + audio.duration
    return video