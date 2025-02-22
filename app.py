import sys

from core import CommandLineParser


if __name__ == "__main__":
    __cli_arguments = CommandLineParser().parse(sys.argv[1:])
    print(__cli_arguments)
