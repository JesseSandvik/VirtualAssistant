from abc import ABC, abstractmethod
from typing import Optional, List

from src.domain.plugin.metadata.plugin_metadata import PluginMetadata


class PluginMetadataLoader(ABC):

    @abstractmethod
    def load(self) -> Optional[List[PluginMetadata]]:
        pass
