from gtts import gTTS


def textToSpeech(full_path, text):
    gttsLang = 'en'
    replyObj = gTTS(text=text,lang=gttsLang,slow=False)
    replyObj.save(full_path)

if __name__ == '__main__':
    textToSpeech("out\\audio\\test.mp3", "Testing! Testing! Testing!")