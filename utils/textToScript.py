from bardapi import Bard
import os
import requests
from configparser import ConfigParser

config = ConfigParser()
readKey = config.read('apidata.config')

print(readKey)
key = readKey["BARD"]["KEY"]

token="xxxxx"
os.environ['_BARD_API_KEY']=key
# os.environ['_BARD_API_KEY']=token

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }

session.cookies.set("__Secure-1PSID", token)


def textToScript1(title, description):
    bard = Bard(token=token, session=session, timeout=30)
    answer = bard.get_answer(f"""
        Throughout this chat you'll act like a professional youtube script writer.
        Generate me a script file for the following title/description. All fields are required at each stamp

        Example:
        
        INPUT FORMAT:
        Title: How to make a youtube video
        Description: In this video I will show you how to make a youtube video. etc...

        OUTPUT FORMAT:
        [TITLE]: How to make a youtube video
        [DESCRIPTION]: In this video I will show you how to make a youtube video.
        [IMAGE]: Youtube logo with black background
        ...


        INPUT:
        TITLE: {title}
        DESCRIPTION: {description}
              
        OUTPUT:
    """)['content']
    
    tokens = answer.split('\n')

    titles = []
    script = []
    images = []

    for token in tokens:
        if token.startswith('-'):
            titles.append(token[2:])
        elif token.startswith('[TITLE]:'):
            script.append(token[8:])
        elif token.startswith('[DESCRIPTION]: '):
            script.append(token[15:])
        elif token.startswith('[IMAGE]: '):
            script.append(token[8:])
    
    script = '\n'.join(script)

    return (titles, script, images)

