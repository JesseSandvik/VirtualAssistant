from abc import ABC, abstractmethod

from src.domain.plugin.entities.plugin_entity import PluginEntity


class IPluginValidator(ABC):

    @abstractmethod
    def validate(self, plugin: PluginEntity) -> None:
        pass
