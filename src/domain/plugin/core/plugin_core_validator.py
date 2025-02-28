from abc import ABC, abstractmethod

from src.domain import PluginCore


class PluginCoreValidator(ABC):

    @abstractmethod
    def validate(self, plugin: PluginCore) -> None:
        pass
