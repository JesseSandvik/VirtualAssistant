import os

from typing import Optional

from core.file_system import FileSystem
from models.plugin import PluginDependency, PluginMetadata, PluginRuntime


class PluginInitializer:
    __IGNORE_DIRECTORIES = ['__pycache__']

    def __init__(self):
        super().__init__()

    def __load_plugin_module_configuration(self, plugin_module_path: str):
        try:
            plugin_module_configuration_data = FileSystem.load_configuration(file_name='plugin.yaml', configuration_directory=plugin_module_path)
            
            plugin_dependencies = []
            for requirement in plugin_module_configuration_data['requirements']:
                plugin_dependencies.append(PluginDependency(**requirement))

            return PluginMetadata(
                name=plugin_module_configuration_data['name'],
                alias=plugin_module_configuration_data['alias'],
                creator=plugin_module_configuration_data['creator'],
                runtime=PluginRuntime(**plugin_module_configuration_data['runtime']),
                repository=plugin_module_configuration_data['repository'],
                description=plugin_module_configuration_data['description'],
                version=plugin_module_configuration_data['version'],
                requirements=plugin_dependencies
            )
        except Exception as e:
            print(f"Error loading plugin module configuration: {e}")
        return None

    def get_initialized_runtime(self, module_name: str, plugin_directory: str = FileSystem.get_plugins_directory()) -> Optional[str]:
        plugin_module_path = os.path.join(plugin_directory, module_name)

        if os.path.isdir(plugin_module_path):
            plugin_metadata: Optional[PluginMetadata] = self.__load_plugin_module_configuration(plugin_module_path=plugin_module_path)

            if plugin_metadata is not None:
                return plugin_metadata.runtime.main
            
        return None
