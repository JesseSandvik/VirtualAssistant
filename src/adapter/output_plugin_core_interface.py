from abc import abstractmethod

from src.domain import IPluginCore


class OutputPluginCoreInterface(IPluginCore):
    
    @abstractmethod
    def send_output(self, response: str):
        pass
