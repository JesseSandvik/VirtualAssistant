import unittest

from core.command_line.parser.command_line_parser import CommandLineParser


class TestCommandLineParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parser = CommandLineParser()

    def test_should_set_log_level_to_debug_by_default(self):
        __cli_arguments = self.parser.parse()
        self.assertEqual(__cli_arguments.log_level, 'DEBUG')
