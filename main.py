# pip uninstall serial
# pip install pyserial

import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os, serial

recognizer = sr.Recognizer()
mic = sr.Microphone()

port = serial.Serial("COM5",9600)

def text_speech(text):
    tts = gTTS(text,lang="tr")
    tts.save("audio.mp3")
    playsound("audio.mp3")
    os.remove("audio.mp3")

def listening():
    with mic as m:
        audio = recognizer.listen(m,phrase_time_limit=4)
        
    try:
        text = recognizer.recognize_google(audio,language="tr-TR").lower()
    except:
        text = "anlayamadım"
    return text

while True:
    ses = listening()
    print(ses)

    if "selamünaleyküm" in ses:
        text_speech("vealeykümselam")

    elif ("mavi" in ses) and ("yak" in ses):
        port.write("1".encode())
        text_speech("mavi led yakıldı")

    elif ("mavi" in ses) and ("kapat" in ses):
        port.write("2".encode())
        text_speech("mavi led kapatıldı")

    elif ("kırmızı" in ses) and ("yak" in ses):
        port.write("3".encode())
        text_speech("kırmızı led yakıldı")

    elif ("kırmızı" in ses) and ("kapat" in ses):
        port.write("4".encode())
        text_speech("kırmızı led kapatıldı")

    elif "çık" in ses:
        text_speech("tamam çıkış yapılıyor")
        port.close()
        break

    else:
        text_speech("anlayamadım")