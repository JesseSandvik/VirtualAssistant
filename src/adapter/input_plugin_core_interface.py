from abc import abstractmethod

from src.domain import IPluginCore


class InputPluginCoreInterface(IPluginCore):

    @abstractmethod
    def get_input(self) -> str:
        pass

    @abstractmethod
    def process_input(self, user_input: str) -> str:
        pass
