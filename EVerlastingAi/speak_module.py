from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    tts = gTTS(text)
    tts.save('D:/DBSuara/speech.mp3')
    playsound('D:/DBSuara/speech.mp3')
    os.remove('D:/DBSuara/speech.mp3')