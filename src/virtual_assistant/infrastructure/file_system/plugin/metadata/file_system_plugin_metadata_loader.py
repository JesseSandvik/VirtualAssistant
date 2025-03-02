import os

from typing import List, Optional

from virtual_assistant.domain.plugin.metadata.plugin_metadata import PluginMetadata
from virtual_assistant.domain.plugin.metadata.plugin_metadata_loader import PluginMetadataLoader

from virtual_assistant.infrastructure.file_system.plugin.file_system_plugin_service import FileSystemPluginSettings, FileSystemPluginService

class FileSystemPluginMetadataLoader(PluginMetadataLoader):

    def __init__(self, plugins_root_directory: str = FileSystemPluginService.get_project_root_directory()):
        super().__init__()
        self.plugins_root_directory = plugins_root_directory

    def __discover_plugin_configuration_files(self) -> Optional[List[str]]:
        plugin_directory = os.path.join(self.plugins_root_directory, 'plugins')
        found_plugins = []

        for root, dirs, files in os.walk(plugin_directory):
            for file in files:
                if file == FileSystemPluginSettings.DEFAULT_PLUGIN_CONFIGURATION_FILE_NAME.value:
                    found_plugins.append(os.path.join(root, file))
        return found_plugins
    
    def __load_plugin_metadata(self, plugin_configuration_file_path: str) -> None:
        plugin_configuration_file_content = FileSystemPluginService.get_yaml_file_contents(plugin_configuration_file_path)
        plugin_metadata = PluginMetadata(
            entry_point=os.path.join(os.path.dirname(plugin_configuration_file_path), plugin_configuration_file_content.get('entry_point')),
            name=plugin_configuration_file_content.get('name'),
            description=plugin_configuration_file_content.get('description'),
            version=plugin_configuration_file_content.get('version'),
            author=plugin_configuration_file_content.get('author'),
            required_python_version=plugin_configuration_file_content.get('required_python_version'),
            compatible_application_versions=plugin_configuration_file_content.get('compatible_application_versions', []),
            dependencies=plugin_configuration_file_content.get('dependencies', []),
            tags=plugin_configuration_file_content.get('tags', [])
        )
        self._add_plugin_metadata(plugin_metadata)

    def load(self):
        plugin_configuration_file_paths = self.__discover_plugin_configuration_files()

        if len(plugin_configuration_file_paths) == 0:
            return

        for plugin_configuration_file_path in plugin_configuration_file_paths:
            self.__load_plugin_metadata(plugin_configuration_file_path)
