import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os




engine=pyttsx3.init('sapi5')

rate=engine.getProperty('rate')
# print(rate)                            #This is too set rate/speed of voice
engine.setProperty('rate',150)

voices=engine.getProperty('voices')
# print(voices)                            #This is to set voice
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<17:
        speak("Good afternoon sir")
    else:
        speak("Good Evening sir")
    speak(" I am Chintu ! How may i help You")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source)
   
    try:
        print("recognising......")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said :{ query }\n")
    except Exception as e:
        print(e)
        print("say someyhing please..")
        return "none"
    return query

if __name__ == "__main__":
    wishme()
    # speak("Hello chintu,how may i help you")
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            # speak("please wait")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to google")
            speak(results)

        elif 'open youtube' in query:
            print(query)
            # c=.get('google-chrome')
            webbrowser.open('http://www.youtube.com')

        elif 'open google' in query:
            print(query)
            webbrowser.open('http://www.google.com')

        elif 'play music' in query:
            music = 'E:\\songs'
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[5]))

        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , The time is {time}")

        elif 'stop' or 'quit' in query:
            break

        else:
            speak("sorry sir did not understand what u said.. please repeat")