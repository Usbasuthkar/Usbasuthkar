from gtts import gTTS
from playsound import playsound
n = input("enter text to be spoken: ")
audio = "speech.mp3"
language = 'en'
sp = gTTS(text = n,lang = language,slow = False)

sp.save(audio)
playsound(audio)
