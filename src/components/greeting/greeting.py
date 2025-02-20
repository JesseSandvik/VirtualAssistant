
class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, my name is {self.name}. Your virtual assistant. How can I be of service?"

    def say_goodbye(self):
        return "Goodbye, and thank you!"
