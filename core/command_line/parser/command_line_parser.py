import logging

from argparse import ArgumentParser


class CommandLineParser:

    def __init__(self):
        self.parser = ArgumentParser()

    def __add_log_level_argument(self):
        self.parser.add_argument(
            "--log-level",
            default="DEBUG",
            choices=list(logging.getLevelNamesMapping()),
            help="set the log level for application",
        )

    def parse(self):
        self.__add_log_level_argument()
        return self.parser.parse_args()
