from abc import ABC, abstractmethod

from src.domain.plugin.plugin_core_interface import IPluginCore


class IPluginCoreValidator(ABC):

    @abstractmethod
    def validate(self, plugin: IPluginCore) -> None:
        pass
