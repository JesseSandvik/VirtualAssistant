from core import CommandLineParser


if __name__ == "__main__":
    __cli_arguments = CommandLineParser().parse()
    print(__cli_arguments)
