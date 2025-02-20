import json
import pyttsx3
import speech_recognition
import webbrowser
import wikipedia

from pathlib import Path

from src.components.greeting.greeting import Greeting

def take_command():
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            print('Recognizing...')
            query = recognizer.recognize_google(audio, language='en-in')
            print('the command is printed=', query)
        except Exception as e:
            print(e)
            print('Something went wrong. Please say that again.')
            return "None"
        
    return query

def test_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice.id)
        engine.setProperty('voice', voice.id)
        engine.say("Hello, I am Ghost. How can I help you?")
        engine.runAndWait()


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Zarvox')
    engine.say(audio)
    engine.runAndWait()


def take_query():
    greeting = Greeting("Ghost")
    speak(greeting.say_hello())

    while True:
        query = take_command().lower()

        if 'test voices' in query:
            test_voices()
            continue

        if 'open google' in query:
            speak("Opening Google...")
            webbrowser.open_new("https://www.google.com")
            continue

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open_new("https://www.youtube.com")
            continue
        
        elif 'tell me your name' in query:
            speak("I am Ghost, your personal assistant.")
            continue

        elif 'search wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(result)
            continue

        elif 'bye' in query:
            speak(greeting.say_goodbye())
            exit()

        return query

if __name__ == "__main__":
    take_query()
