import pyttsx3
#import pyaudio
import speech_recognition as sr
import datetime
import os
import project_speech as ps

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=5)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    
    except Exception as e:
        speak("Say that again please...")
        return "none"
    
    return query

# greetings
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning")
    elif 12 <= hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis, how can I assist you?")

if __name__ == "__main__":
    #speak("Hello Sir")
    #takecommand()
    wish()
    #speak("This is advance jarvis")
    #while True:
    if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(npath)
        
        elif "explain project" in query:
            speak(ps.proj_speech[1])