import random

class Banter:
    def __init__(self, name: str, greetings: list[str], sign_offs: list[str]):
        self.name = name
        self.greetings = greetings
        self.sign_offs = sign_offs

    def __get_random_greeting(self) -> str:
        return random.choice(self.greetings)
    
    def __get_random_sign_off(self) -> str:
        return random.choice(self.sign_offs)
    
    def say_name(self) -> str:
        return f"My name is {self.name}"

    def say_hello(self) -> str:
        return self.__get_random_greeting().replace('[NAME]', self.name)

    def say_goodbye(self) -> str:
        return self.__get_random_sign_off().replace('[NAME]', self.name)

