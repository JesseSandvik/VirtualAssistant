from typing import Dict, List, Optional

from virtual_assistant.domain.plugin.metadata.plugin_metadata import PluginMetadata
from virtual_assistant.domain.plugin.metadata.plugin_metadata_repository import PluginMetadataRepository

from virtual_assistant.infrastructure.file_system.file_system_service import FileSystemService

class FileSystemPluginMetadataRepository(PluginMetadataRepository):
    __plugin_metadata: Dict[str, PluginMetadata]

    def __init__(self, file_system_plugin_metadata_file_path: str):
        self.__plugin_metadata = {}

    def __load_existing_plugin_metadata_from_file_system(self, file_system_plugin_metadata_file_path: str) -> Optional[Dict[str, PluginMetadata]]:
        # TODO: load existing plugin metadata from the file system on init
        pass

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
