import inspect
import os

from importlib import import_module
from typing import List

from src.infrastructure import FileSystem, FileSystemConfiguration
from src.application import PluginManager


class PluginLoader:
    __IGNORE_DIRECTORIES = ['__pycache__']
    __IGNORE_FILES = ['__init__.py']

    def __init__(self, plugin_manager: PluginManager):
        self.plugin_manager = plugin_manager

    @staticmethod
    def __discover_plugin_paths() -> List[str]:
        plugin_paths = []
        for root, dirs, files in os.walk(FileSystem.get_plugins_directory()):
            dirs[:] = [d for d in dirs if d not in PluginLoader.__IGNORE_DIRECTORIES]

            for file in files:
                if file.endswith(".py") and file not in PluginLoader.__IGNORE_FILES:
                    plugin_paths.append(os.path.join(root, file))

        return plugin_paths
    
    @staticmethod
    def __get_plugin_configuration_from_plugin_file_path(plugin_file_path: str):
        plugin_candidate_entry_point = FileSystem.get_file_name_from_path(plugin_file_path)
        plugin_candidate_configuration_file_path = plugin_file_path.replace(plugin_candidate_entry_point, FileSystemConfiguration.PLUGIN_CONFIGUATION_FILE_NAME.value)
        return FileSystem.load_configuration(plugin_candidate_configuration_file_path)

    @staticmethod
    def __get_plugin_module_from_plugin_file_path(plugin_file_path: str):
        plugin_module_path = FileSystem.get_file_path_after_root_directory(plugin_file_path)
        plugin_module_path_without_file_extension = FileSystem.remove_file_extension(plugin_module_path)
        plugin_module_import_path = '.'.join(FileSystem.get_path_sections(plugin_module_path_without_file_extension))
        return import_module(plugin_module_import_path)

    def load_plugins(self) -> List[str]:
        plugin_candidate_file_paths = PluginLoader.__discover_plugin_paths()

        for plugin_candidate_file_path in plugin_candidate_file_paths:
            plugin_candidate_configuration = PluginLoader.__get_plugin_configuration_from_plugin_file_path(plugin_candidate_file_path)

            if plugin_candidate_configuration.get('enabled', False):
                try:
                    plugin_module = PluginLoader.__get_plugin_module_from_plugin_file_path(plugin_candidate_file_path)

                    for name, obj in inspect.getmembers(plugin_module, inspect.isclass):
                        if obj.__module__ == plugin_module.__name__:
                            self.plugin_manager.register_plugin(name, obj)
                except Exception as e:
                    print(f"Error loading plugin {plugin_candidate_file_path}: {e}")
