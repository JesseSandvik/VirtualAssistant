import logging
import pyttsx3
import speech_recognition


LOGGER = logging.getLogger(__name__)


class Bot:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def test_voices(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            LOGGER.info(f"[{self.name}] speaking in voice: {voice}")
            engine.setProperty('voice', voice.id)
            engine.say(f"Hello, I am {self.name}. How can I help you?")
            engine.runAndWait()

    def take_command(self):
        recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
            LOGGER.info(f"[{self.name}] is listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)
            try:
                query = recognizer.recognize_google(audio, language='en-in')
            except Exception as e:
                print(e)
                print('Something went wrong.')
                return "None"
            
        return query

    def speak(self, audio: str, voice: str, speech_rate: int):
        engine = pyttsx3.init()
        engine.setProperty('rate', speech_rate)
        engine.setProperty('voice', voice)
        LOGGER.info(f"[{self.name}] says: {audio}")
        engine.say(audio)
        engine.runAndWait()
