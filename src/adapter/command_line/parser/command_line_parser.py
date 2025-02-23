import logging

from argparse import ArgumentParser

from src.adapter.command_line.models import CommandLineParameters

class CommandLineParser:

    def __init__(self, description: str = None, usage: str = None):
        self.parser = ArgumentParser(description=description, usage=usage)
        self.__add_log_level_argument()

    def __add_log_level_argument(self):
        self.parser.add_argument(
            "--log-level",
            default="INFO",
            choices=list(logging.getLevelNamesMapping()),
            help="set the log level for the application",
        )

    def parse(self, args) -> CommandLineParameters:
        known_args = self.parser.parse_args(args)
        return CommandLineParameters(log_level=known_args.log_level)
