import unittest

from core.command_line.parser.command_line_parser import CommandLineParser


class TestCommandLineParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parser = CommandLineParser()

    def test_should_set_log_level_to_INFO_by_default(self):
        __cli_arguments = self.parser.parse([])
        self.assertEqual(__cli_arguments.log_level, 'INFO')

    def test_should_set_log_level_to_INFO_when_specified(self):
        __cli_arguments = self.parser.parse(['--log-level=INFO'])
        self.assertEqual(__cli_arguments.log_level, 'INFO')

    def test_should_set_log_level_to_WARNING_when_specified(self):
        __cli_arguments = self.parser.parse(['--log-level=WARNING'])
        self.assertEqual(__cli_arguments.log_level, 'WARNING')

    def test_should_set_log_level_to_ERROR_when_specified(self):
        __cli_arguments = self.parser.parse(['--log-level=ERROR'])
        self.assertEqual(__cli_arguments.log_level, 'ERROR')

    def test_should_set_log_level_to_CRITICAL_when_specified(self):
        __cli_arguments = self.parser.parse(['--log-level=CRITICAL'])
        self.assertEqual(__cli_arguments.log_level, 'CRITICAL')

    def test_should_set_log_level_to_DEBUG_when_specified(self):
        __cli_arguments = self.parser.parse(['--log-level=DEBUG'])
        self.assertEqual(__cli_arguments.log_level, 'DEBUG')

    def test_should_set_log_level_to_NOTSET_when_specified(self):
        __cli_arguments = self.parser.parse(['--log-level=NOTSET'])
        self.assertEqual(__cli_arguments.log_level, 'NOTSET')
