import json
import logging
import os
import webbrowser
import wikipedia

from pathlib import Path

from src.app.bot.bot import Bot
from src.app.banter.banter import Banter

FORMAT = '%(asctime)s - %(levelname)s | %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

LOGGER = logging.getLogger(__name__)


def take_query():
    assistant_config_file_path = os.path.join(
        os.path.dirname(__file__),
        'src',
        'config',
        'assistant.json'
    )
    assistant_config_file_content = Path(assistant_config_file_path).read_text()
    assistant_config = json.loads(assistant_config_file_content)
    bot = Bot(name=assistant_config.get('name'))

    banter = Banter(
         name=bot.get_name(),
         greetings=assistant_config.get('greetings'),
         sign_offs=assistant_config.get('sign_offs')
    )
    bot.speak(audio=banter.say_hello(), voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))

    while True:
        query = bot.take_command().lower()

        if 'test voices' in query:
            bot.test_voices()
            continue

        if 'open google' in query:
            bot.speak(audio="Opening Google...", voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            webbrowser.open_new("https://www.google.com")
            continue

        elif 'open youtube' in query:
            bot.speak(audio="Opening YouTube...", voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            webbrowser.open_new("https://www.youtube.com")
            continue
        
        elif 'what is your name' in query:
            bot.speak(audio=banter.say_name(), voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            continue

        elif 'search wikipedia' in query:
            bot.speak(audio="Searching Wikipedia...", voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            bot.speak(audio="According to Wikipedia...", voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            bot.speak(audio=result, voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            continue

        elif 'bye' in query:
            bot.speak(audio=banter.say_goodbye(), voice=assistant_config.get('maleVoice'), speech_rate=assistant_config.get('speechRate'))
            exit()

        return query

if __name__ == "__main__":
    take_query()
