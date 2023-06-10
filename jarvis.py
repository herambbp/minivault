import speech_recognition as sr
import os
import win32com.client
import webbrowser

speaker = win32com.client.Dispatch("SAPI.SpVoice")      

def say(text):
    speaker.speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio,language="en-in")
            print(query)
            return query
        except Exception as e:
            return "Some error occured...Sorry from MINIVAULT"

def voice_input():
    print("Listening...")
    query = takeCommand()
    return query