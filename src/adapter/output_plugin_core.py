from abc import abstractmethod

from src.domain import PluginCore


class OutputPluginCore(PluginCore):
    
    @abstractmethod
    def send_output(self, response: str):
        pass
