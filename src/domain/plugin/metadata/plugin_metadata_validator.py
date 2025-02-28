from abc import ABC, abstractmethod

from src.domain import PluginMetadata


class PluginMetadataValidator(ABC):

    @abstractmethod
    def validate(self, plugin_metadata: PluginMetadata) -> None:
        pass
