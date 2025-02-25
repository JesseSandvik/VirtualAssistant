from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.plugin.entities.plugin_metadata_entity import PluginMetadataEntity


class IPluginMetadataRepository(ABC):

    @abstractmethod
    def save(self, plugin_metadata: PluginMetadataEntity) -> None:
        pass
    
    @abstractmethod
    def get(self, id: str) -> Optional[PluginMetadataEntity]:
        pass
    
    @abstractmethod
    def list(self) -> List[PluginMetadataEntity]:
        pass
    
    @abstractmethod
    def remove(self, id: str) -> None:
        pass
    
    @abstractmethod
    def exists(self, id: str) -> bool:
        pass
