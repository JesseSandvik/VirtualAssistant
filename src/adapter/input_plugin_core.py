from abc import abstractmethod

from src.domain.plugin.core import PluginCore


class InputPluginCore(PluginCore):

    @abstractmethod
    def get_input(self) -> str:
        pass

    @abstractmethod
    def process_input(self, user_input: str) -> str:
        pass
