import tempfile

from typing import Dict, List, Optional

from virtual_assistant.domain.plugin.metadata.plugin_metadata import PluginMetadata
from virtual_assistant.domain.plugin.metadata.plugin_metadata_repository import PluginMetadataRepository

from virtual_assistant.infrastructure.file_system.file_system_service import FileSystemService

class FileSystemPluginMetadataRepository(PluginMetadataRepository):

    def __init__(self, file_system_plugin_metadata_file_path: str):
        self.__plugin_metadata: Dict[str, PluginMetadata] = self.__load_existing_plugin_metadata_from_file_system(file_system_plugin_metadata_file_path)

    def __load_existing_plugin_metadata_from_file_system(self, file_system_plugin_metadata_file_path: str) -> Optional[Dict[str, PluginMetadata]]:
        plugin_metadata_from_file_system = FileSystemService.get_json_file_content(file_system_plugin_metadata_file_path)
        print(f'temp file path: {tempfile.gettempdir()}')
        repository_plugin_metadata = {}
        for plugin_metadata in plugin_metadata_from_file_system:
            for key, value in plugin_metadata.items():
                repository_plugin_metadata[key] = PluginMetadata(
                    entry_point=value.get('entry_point'),
                    name=value.get('name'),
                    description=value.get('description'),
                    version=value.get('version'),
                    author=value.get('author'),
                    required_python_version=value.get('required_python_version'),
                    user_enabled=value.get('enabled'),
                    compatible_application_versions=value.get('compatible_python_versions', []),
                    dependencies=value.get('dependencies', []),
                    tags=value.get('tags', [])
                )
        print(repository_plugin_metadata)
        return repository_plugin_metadata

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
