from abc import abstractmethod

from src.domain import PluginCoreInterface


class OutputPluginCoreInterface(PluginCoreInterface):
    
    @abstractmethod
    def send_output(self, response: str):
        pass
