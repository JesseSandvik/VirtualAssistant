import sys

from core import CommandLineParser


def __initialize_application():
    pass


if __name__ == "__main__":
    __cli_arguments = CommandLineParser().parse(sys.argv[1:])
    print(__cli_arguments.log_level)
    __initialize_application()
