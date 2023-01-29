from datetime import datetime
import winsound
from playsound import playsound
from gtts import gTTS
def alarm_12(hour,min,ap,n):
    a = datetime.now()
    ch = a.hour
    cm = a.minute
    cs = a.second
    flag = 0
    tag = 0
    language = 'en'
    AP = ap.upper() 
    audio = "speech.mp3"
    if hour <= 12:
        if AP == 'PM':
            h = hour + 12
            if hour == 12 and min > cm and h == 24:
                if hour > ch:
                    print("your alarm is set for next", hour - ch, "hours and", min - cm, "minutes")
                else:
                    print("your alarm is set for next", ch - hour, "hours and", min - cm, "minutes")
            elif hour == 12 and cm > min and h == 24:
                if hour > ch:
                    print("your alarm is set for next", hour - ch - 1, "hours and", 60 - (cm - min), "minutes")
                else:
                    print("your alarm is set for next", ch - hour - 1, "hours and", 60 - (min - cm), "minutes")
            elif min >= cm and h >= ch:
                print("your alarm is set for next", h - ch, "hours and", min - cm, "minutes")
            elif min >= cm and h <= ch:
                print("your alarm is set for next", 12 - (ch - h), "hours and", min - cm, "minutes")
            elif cm >= min and ch >= h:
                print("your alarm is set for next", 12 - (h - ch) - 1, "hours and", 60 - (cm - min),
                      "minutes")
            elif min <= cm and h >= ch:
                print("your alarm is set for next", (h - ch) - 1, "hours and", 60 - (cm - min), "minutes")
            else:
                flag = 1
        else:
            if ch >= 12:
                ih = ch - 12
                if min >= cm and hour >= ih:
                    print("your alarm is set for next", hour - ih, "hours and", min - cm, "minutes")
                elif min >= cm and hour <= ch:
                    print("your alarm is set for next", 12 - (ih - hour), "hours and", min - cm, "minutes")
                elif cm >= min and ih >= hour:
                    print("your alarm is set for next", 12 - (hour - ih) - 1, "hours and", 60 - (cm - min),
                          "minutes")
                elif min <= cm and hour >= ih:
                    print("your alarm is set for next", (hour - ih) - 1, "hours and", 60 - (cm - min), "minutes")
                else:
                    flag = 1
            elif ch == 0:
                a = ch + 12
                if min >= cm and hour >= a:
                    print("your alarm is set for next", hour - a, "hours and", min - cm, "minutes")
                elif min >= cm and hour <= a:
                    print("your alarm is set for next", 12 - (a - hour), "hours and", min - cm, "minutes")
                elif min <= cm and hour >= a:
                    print("your alarm is set for next", (hour - a) - 1, "hours and", 60 - (cm - min), "minutes")
                elif min <= cm and hour <= a:
                    print("your alarm is set for next", 12 - (a - hour) - 1, "hours and", 60 - (cm - min), "minutes")
                else:
                    flag = 1
            else:
                if min >= cm and hour >= ch:
                    print("your alarm is set for next", hour - ch, "hours and", min - cm, "minutes")
                elif min >= cm and hour <= ch:
                    print("your alarm is set for next", 24 - (ch - hour), "hours and", min - cm, "minutes")
                elif min <= cm and hour >= ch:
                    print("your alarm is set for next", (hour - ch) - 1, "hours and", 60 - (cm - min), "minutes")
                elif min <= cm and hour <= ch:
                    print("your alarm is set for next", 24 - (ch - hour) - 1, "hours and", 60 - (cm - min), "minutes")
                else:
                    flag = 1
        if flag == 1:
            print("invalid time")
    if flag != 1:
        while True:
            a = datetime.now()
            ch = a.hour
            cm = a.minute
            cs = a.second
            if AP == 'PM':
                if hour < 12 and min <= 60:
                    hour1 = hour + 12
                    if hour1 == ch and min == cm:
                        sp = gTTS(text=n,lang = language,slow=False)
                        sp.save(audio)
                        playsound(audio)
                        #winsound.Beep(10000, 300)
                        break
                elif hour == 12 and min <= 60:
                    hour1 = hour
                    if hour1 == ch and min == cm:
                        sp = gTTS(text=n,lang = language,slow=False)
                        sp.save(audio)
                        playsound(audio)
                        #winsound.Beep(10000, 300)
                        break
                else:
                    tag = 1
                    break
            else:
                if hour < 12 and min <= 60:
                    if hour == ch and min == cm:
                        sp = gTTS(text=n, lang=language, slow=False)
                        sp.save(audio)
                        playsound(audio)
                        #winsound.Beep(10000, 300)
                        break
                elif hour == 12 and min <= 60:
                    hour = 0
                    if hour == ch and min == cm:
                        sp = gTTS(text=n, lang=language, slow=False)
                        sp.save(audio)
                        playsound(audio)
                        #winsound.Beep(10000, 300)
                        break
                else:
                    tag = 1
                    break
        if tag == 1:
            print("invalid time")
def alarm_24(hour,min,n):
    a = datetime.now()
    ch = a.hour
    cm = a.minute
    cs = a.second
    flag = 0
    tag = 0
    language = 'en'
    audio = "speech.mp3"
    if min>=cm and hour>=ch:
        print("your alarm is set for next",hour - ch,"hours and",min - cm,"minutes")
    elif min>=cm and hour<=ch:
        print("your alarm is set for next", 24-(ch - hour), "hours and", min - cm, "minutes")
    elif min<=cm and hour>=ch:
        print("your alarm is set for next",(hour-ch)-1,"hours and",60-(cm - min),"minutes")
    elif min<=cm and hour<=ch:
        print("your alarm is set for next",24-(ch-hour)-1,"hours and",60-(cm - min),"minutes")
    else:
        flag = 1
    if flag == 1:
        print("invalid time")
    if flag!=1:
        while True:
            a = datetime.now()
            ch = a.hour
            cm = a.minute
            cs = a.second
            if hour <= 24 and min <= 60:
                if hour == ch and min == cm:
                    sp = gTTS(text=n, lang=language, slow=False)
                    sp.save(audio)
                    playsound(audio)
                    #winsound.Beep(10000, 300)
                    break
            else:
                tag = 1
                break
        if tag == 1:
            print("invalid time")
a = datetime.now()
ch = a.hour
cm = a.minute
cs = a.second
print("current hour: ",ch)
print("current minutes: ",cm)
print("Current seconds: ",cs)
choose = input("press 'I' for 12 hours format or by default its 24 hour(press any key): ")
hour = int(input("Enter hour: "))
min = int(input("Enter min: "))
n = input("enter text: ")
if choose == 'I' or choose == 'i':
    ap = input("AM or PM:")
    alarm_12(hour,min,ap,n)
else:
    alarm_24(hour,min,n)