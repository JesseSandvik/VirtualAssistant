

class PluginEngine:

    def __init__(self, **args):
        pass

    def __reload_plugins(self) -> None:
        pass

    def __invoke_on_plugins(self, command: chr) -> None:
        pass

    def run(self) -> None:
        self.__reload_plugins()
        self.__invoke_on_plugins('r')
