import speech_recognition as sr

r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold()
    print("say anything : ")
    audio= r.listen(source)
    print("Stop")
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("sorry, could not recognise")