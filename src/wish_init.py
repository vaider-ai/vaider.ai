import datetime
from speak import speak

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")    

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")       

    else:
        speak("Good Evening!")      

    speak('how may I help you')