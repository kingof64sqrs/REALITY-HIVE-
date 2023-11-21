from googletrans import Translator
from gtts import gTTS
import os

# pip install googletrans==4.0.0-rc1 gtts

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("start output.mp3")

# Example usage:
input_text = "Hello, how are you?"
target_language = 'es'  # Spanish

# Translate text
translated_text = translate_text(input_text, target_language)
print(f"Translated Text: {translated_text}")

# Convert translated text to speech
text_to_speech(translated_text, lang=target_language)
