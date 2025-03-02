from abc import ABC, abstractmethod

from .plugin_metadata import PluginMetadata

class PluginMetadataBaseValidator(ABC):

    def __init__(self, next_validator = None):
        self.next_validator = next_validator

    @abstractmethod
    def _check(self, plugin_metadata: PluginMetadata) -> None:
        pass

    def validate(self, plugin_metadata: PluginMetadata) -> None:
        self._check(plugin_metadata)
        if self.next_validator:
            self.next_validator.validate(plugin_metadata)
