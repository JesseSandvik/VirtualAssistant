from typing import Dict, List, Optional

from virtual_assistant.domain.plugin.metadata.plugin_metadata import PluginMetadata
from virtual_assistant.domain.plugin.metadata.plugin_metadata_repository import PluginMetadataRepository

class FileSystemPluginMetadataRepository(PluginMetadataRepository):

    def create_plugin_metadata(self, plugin_metadata: PluginMetadata) -> Optional[PluginMetadata]:
        pass

    def get_plugin_metadata_by_entry_point(self, entry_point: str) -> Optional[PluginMetadata]:
        pass

    def get_all_plugin_metadata(self) -> List[Dict[str, PluginMetadata]]:
        pass

    def update_plugin_metadata_by_entry_point(self, entry_point: str) -> Optional[PluginMetadata]:
        pass

    def remove_plugin_metadata_by_entry_point(self, entry_point: str) -> bool:
        pass
