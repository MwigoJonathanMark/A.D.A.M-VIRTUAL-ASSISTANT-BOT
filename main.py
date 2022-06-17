#! python3.9

import os
# import google
import smtplib
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr

MASTER = "Sir"
CHROME_PATH = "C:/Program Files (x86)/Google/Application/chrome.exe %s"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak(f"...Good Morning {MASTER}, how may i help you?")
    elif hour >= 12 and hour < 18:
        speak(f"...Good Afternoon {MASTER}, how may i help you?")
    else:
        speak(f"...Good Evening {MASTER}, how may i help you?")

def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = str(r.recognize_google(audio, language="en-ug"))
        # print(f"user said: {query}\n")
    except Exception as e:
        speak("...I didn't get you..., please come again!")
        # speak(e)
        print(e)
        take_commands()
        # query = None
        query = ""

    return query
    
def command_handler(query):
    if "wikipedia" in query.lower():
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=4)
        speak(results)
    elif "open chrome" in query.lower():
        webbrowser.get(CHROME_PATH).open("google.com")
    elif "open youtube" in query.lower():
        webbrowser.get(CHROME_PATH).open("youtube.com")
    elif "open github" in query.lower():
        webbrowser.open("github.com")
    elif "open face book" in query.lower():
        webbrowser.get(CHROME_PATH).open("facebook.com")
    elif "open reddit" in query.lower():
        webbrowser.get(CHROME_PATH).open("reddit.com")
    elif "open music" in query.lower():
        pass
    elif "open movies and tv" in query.lower():
        pass
    elif "play music" in query.lower():
        songs_dir = "D:/my music"
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir, songs[6]))
    elif "the time" in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"...the time is {strTime}")
    elif "am bored" in query.lower():
        speak("Oohh... really... how may i be of help...?")
    elif "adam" in query.lower():
        speak("Yes please... how may i help you...?")

while True:
    greeting()
    # speak("Hello Jonathan..., How are you?")
    query = take_commands()
    print(f"user said: {query}\n")
    command_handler(query)
    # print(voices)
# python "C:\Users\MWIGO-JON-MARK\Desktop\PYTHON PROJECTS\PROJECT_A.D.A.M\main.py"
