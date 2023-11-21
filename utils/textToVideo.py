from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
from moviepy import editor
from flask import send_file
import os
from .textToSpeech import textToSpeech as tts
from .textToScript import textToScript
from .downloadImages import download_unsplash_image

def create_video_from_text(get_path, folder_path, text, audio_path, video_path):
    description = textToScript(text)

    # Creating the audio file
    print("Creating Text To Speech")
    tts(os.path.join(get_path, audio_path), description)

    # download free stock images
    print("Downloading images...")
    download_unsplash_image(keyword=title, full_path=get_path)

    # Creating the video file
    print("Creating video")
    return create_video(get_path, folder_path, audio_path, video_path)



def create_video(get_path, folder_path, audio_path, video_path):
    full_audio_path = os.path.join(get_path, audio_path)
    full_video_path = os.path.join(get_path, video_path)

    # Reading in the mp3 that we got from gTTS
    song = MP3(full_audio_path)
    audio_length = round(song.info.length)

    # Globbing the images and Stitching it to for the gif
    path_images = Path(folder_path)
    images = list(path_images.glob('*.jpg'))
    image_list = list()

    for image_name in images:
        image = Image.open(image_name).resize((1600, 900), Image.Resampling.LANCZOS)
        image_list.append(image)

    # Checking Audio length
    length_audio = audio_length
    duration = int(length_audio / len(image_list)) * 1000

    # Creating Gif
    image_list[0].save(os.path.join(folder_path, "temp.gif"),
                       save_all=True,
                       append_images=image_list[1:],
                       duration=duration)

    # Creating the video using the gif and the audio file
    video = editor.VideoFileClip(os.path.join(folder_path, "temp.gif"))
    audio = editor.AudioFileClip(full_audio_path)
    final_video = video.set_audio(audio)
    final_video.set_fps(24)
    final_video.write_videofile(full_video_path)

    return video_path

if __name__ == "__main__":
    create_video_from_text(
        get_path=r'D:\Programs Related\Team Project\gdsc-project\out',
        folder_path=r'D:\Programs Related\Team Project\gdsc-project\out\file',
        text="""The Bayer test is a chemical test used to identify the presence of phenolic hydroxyl groups in organic compounds. Here's a step-by-step explanation in short and crisp terms""",
        audio_path="file\\output.mp3",
        video_path="file\\output.mp4")