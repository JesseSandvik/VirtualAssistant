from abc import ABC, abstractmethod

from .plugin_metadata import PluginMetadata

class PluginMetadataValidator(ABC):

    @abstractmethod
    def validate(self, metadata: PluginMetadata) -> None:
        pass
