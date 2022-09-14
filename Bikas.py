import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant sir. Please tell me how may I help you")

def takecommand():
    #takes microphone input from the user and return string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognising....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query    




if __name__ =="__main__":
    wishme()
    while True:
        query=takecommand().lower()  

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='E:\\Music\\relax'
            songs=os.listdir(music_dir)
            #Print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Hi, the time is {strtime}")
        elif 'open vscode' in query:
            vscode="C:\\Users\\PS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscode)
        elif 'quit' in query:
            print("Quitting Sir")
            speak("Quitting Sir")
            exit()
