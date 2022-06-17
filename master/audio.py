import pyttsx3
from moviepy.editor import AudioFileClip, CompositeAudioClip, concatenate_audioclips

# Convert text into speech and save it to given path
def to_speech(text: str, path: str) -> None:
    tts = pyttsx3.Engine()
    tts.save_to_file(text, path)
    tts.runAndWait()

# Concatenate multiple audios into one
def concatenate_audios(audio_files: list) -> CompositeAudioClip:
    silence = AudioFileClip('assets/silence.mp3')
    audios = [AudioFileClip(a) for a in audio_files]
    clips = [silence] * (len(audios) * 2 - 1)
    clips[0::2] = audios

    return concatenate_audioclips(clips)