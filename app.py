import sys

from core import CommandLineParser, PluginInitializer


def __initialize_application():
    configured_plugin_runtime = PluginInitializer().get_initialized_runtime(module_name='speech-interface-plugin')
    print(configured_plugin_runtime)


if __name__ == "__main__":
    __cli_arguments = CommandLineParser().parse(sys.argv[1:])
    print(__cli_arguments.log_level)
    __initialize_application()
