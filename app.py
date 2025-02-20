import json
import os
import pyttsx3
import speech_recognition
import webbrowser
import wikipedia

from pathlib import Path

from src.app.banter.banter import Banter

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


def speak(audio: str, voice: str, speech_rate: int):
    engine = pyttsx3.init()
    engine.setProperty('rate', speech_rate)
    engine.setProperty('voice', voice)
    engine.say(audio)
    engine.runAndWait()


def take_query():
    assistant_config_file_path = os.path.join(
        os.path.dirname(__file__),
        'src',
        'config',
        'assistant.json'
    )
    assistant_config_file_content = Path(assistant_config_file_path).read_text()
    assistant_config = json.loads(assistant_config_file_content)

    banter = Banter(
         name=assistant_config.get('name'),
         greetings=assistant_config.get('greetings'),
         sign_offs=assistant_config.get('sign_offs')
    )
    speak(audio=banter.say_hello(), voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))

    while True:
        query = take_command().lower()

        if 'test voices' in query:
            test_voices()
            continue

        if 'open google' in query:
            speak(audio="Opening Google...", voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            webbrowser.open_new("https://www.google.com")
            continue

        elif 'open youtube' in query:
            speak(audio="Opening YouTube...", voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            webbrowser.open_new("https://www.youtube.com")
            continue
        
        elif 'tell me your name' in query:
            speak(audio=banter.say_name(), voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            continue

        elif 'search wikipedia' in query:
            speak(audio="Searching Wikipedia...", voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(audio="According to Wikipedia...", voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            speak(audio=result, voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            continue

        elif 'bye' in query:
            speak(audio=banter.say_goodbye(), voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            exit()

        return query

if __name__ == "__main__":
    take_query()
