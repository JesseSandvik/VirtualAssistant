from abc import ABC, abstractmethod
from typing import Dict

from .plugin_metadata import PluginMetadata

class PluginMetadataLoader(ABC):

    @abstractmethod
    def load(self) -> Dict[str, PluginMetadata]:
        pass
