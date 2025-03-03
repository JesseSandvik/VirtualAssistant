from abc import ABC, abstractmethod
from typing import Dict, Optional

from .plugin_metadata import PluginMetadata


class PluginMetadataRepository(ABC):
    __plugin_metadata: Dict[str, PluginMetadata]

    @abstractmethod
    def save(self, plugin_metadata: PluginMetadata) -> None:
        self.__plugin_metadata[plugin_metadata.entry_point] = plugin_metadata
    
    @abstractmethod
    def get_plugin_metadata_by_entry_point(self, entry_point: str) -> Optional[PluginMetadata]:
        return self.__plugin_metadata.get(entry_point, None)
    
    @abstractmethod
    def get_all_plugin_metadata(self) -> Dict[str, PluginMetadata]:
        return self.__plugin_metadata.items()
    
    @abstractmethod
    def remove_plugin_metadata_by_entry_point(self, entry_point: str) -> None:
        self.__plugin_metadata.pop(entry_point, None)
    
    @abstractmethod
    def exists(self, entry_point: str) -> bool:
        return entry_point in self.__plugin_metadata.keys()
