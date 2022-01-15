from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    tts = gTTS(text)
    tts.save('C:/Users/Yukino Arata/Music/DBSuara/speech.mp3')
    playsound('C:/Users/Yukino Arata/Music/DBSuara/speech.mp3')