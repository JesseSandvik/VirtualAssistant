from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from .plugin_metadata import PluginMetadata


class PluginMetadataRepository(ABC):

    @abstractmethod
    def create_plugin_metadata(self, plugin_metadata: PluginMetadata) -> Optional[PluginMetadata]:
        pass
    
    @abstractmethod
    def get_plugin_metadata_by_entry_point(self, entry_point: str) -> Optional[PluginMetadata]:
        pass
    
    @abstractmethod
    def get_all_plugin_metadata(self) -> Optional[List[Dict[str, PluginMetadata]]]:
        pass

    @abstractmethod
    def update_plugin_metadata_by_entry_point(self, entry_point: str, plugin_metadata: PluginMetadata) -> Optional[PluginMetadata]:
        pass
    
    @abstractmethod
    def remove_plugin_metadata_by_entry_point(self, entry_point: str) -> bool:
        pass
