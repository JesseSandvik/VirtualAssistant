from abc import ABC, abstractmethod

from src.domain.plugin.core.plugin_core import PluginCore


class PluginCoreValidator(ABC):

    @abstractmethod
    def validate(self, plugin: PluginCore) -> None:
        pass
