from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.plugin.metadata.plugin_metadata import PluginMetadata


class PluginMetadataRepository(ABC):

    @abstractmethod
    def save(self, plugin_metadata: PluginMetadata) -> None:
        pass
    
    @abstractmethod
    def get(self, id: str) -> Optional[PluginMetadata]:
        pass
    
    @abstractmethod
    def list(self) -> List[PluginMetadata]:
        pass
    
    @abstractmethod
    def remove(self, id: str) -> None:
        pass
    
    @abstractmethod
    def exists(self, id: str) -> bool:
        pass
