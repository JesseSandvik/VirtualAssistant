from abc import ABC, abstractmethod
from typing import Optional, List

from src.domain.plugin.metadata.plugin_metadata import PluginMetadata


class PluginMetadataLoader(ABC):

    def __init__(self):
        self.plugin_metadata = []

    @abstractmethod
    def load(self) -> Optional[List[PluginMetadata]]:
        pass
