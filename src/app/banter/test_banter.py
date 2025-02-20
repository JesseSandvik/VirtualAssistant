import unittest

from src.app.banter.banter import Banter


class TestBanter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.banter = Banter(
            name='Atom',
            greetings=['Hello, my name is Atom'],
            sign_offs=['Goodbye']
        )

    def test_should_say_hello(self):
        actual = self.banter.say_hello()
        self.assertIn('Hello', actual)

    def test_should_contain_name_in_greeting(self):
        actual = self.banter.say_hello()
        self.assertIn('Atom', actual)

    def test_should_say_name(self):
        actual = self.banter.say_name()
        self.assertEqual('My name is Atom.', actual)

    def test_should_say_goodbye(self):
        actual = self.banter.say_goodbye()
        self.assertIn('Goodbye', actual)
