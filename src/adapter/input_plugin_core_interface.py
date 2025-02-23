from abc import abstractmethod

from src.domain import PluginCoreInterface


class InputPluginCoreInterface(PluginCoreInterface):

    @abstractmethod
    def get_input(self) -> str:
        pass

    @abstractmethod
    def process_input(self, user_input: str) -> str:
        pass
