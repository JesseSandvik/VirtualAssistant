import inspect
import os

from importlib import import_module

from src.infrastructure import FileSystem, FileSystemConfiguration
from src.domain import PluginRegistry
from typing import List


class PluginLoader:
    __IGNORE_DIRECTORIES = ['__pycache__']
    __IGNORE_FILES = ['__init__.py']

    def __init__(self, plugin_registry: PluginRegistry):
        self.plugin_registry = plugin_registry

    @staticmethod
    def __filter_ignored_plugin_paths() -> List[str]:
        plugin_paths = []
        for root, dirs, files in os.walk(FileSystem.get_plugins_directory()):
            dirs[:] = [d for d in dirs if d not in PluginLoader.__IGNORE_DIRECTORIES]

            for file in files:
                if file.endswith(".py") and file not in PluginLoader.__IGNORE_FILES:
                    plugin_paths.append(os.path.join(root, file))

        return plugin_paths
    
    def discover_plugins(self) -> List[str]:
        plugin_candidates = PluginLoader.__filter_ignored_plugin_paths()
        print(plugin_candidates)

        for plugin_candidate in plugin_candidates:
            plugin_candidate_entry_point = FileSystem.get_file_name_from_path(plugin_candidate)
            plugin_candidate_configuration_file_path = plugin_candidate.replace(plugin_candidate_entry_point, FileSystemConfiguration.PLUGIN_CONFIGUATION_FILE_NAME.value)
            plugin_candidate_configuration = FileSystem.load_configuration(plugin_candidate_configuration_file_path)

            if plugin_candidate_configuration.get('enabled'):
                try:
                    plugin_module_path = FileSystem.get_file_path_after_root_directory(plugin_candidate)
                    plugin_module_path_without_file_extension = FileSystem.remove_file_extension(plugin_module_path)
                    plugin_module_import_path = '.'.join(FileSystem.get_path_sections(plugin_module_path_without_file_extension))
                    print('='*100)
                    print(plugin_module_import_path)
                    print('='*100)
                    plugin_module = import_module(plugin_module_import_path)

                    for name, obj in inspect.getmembers(plugin_module, inspect.isclass):
                        if obj.__module__ == plugin_module.__name__:
                            self.plugin_registry.register_plugin(name, obj)
                    print(self.plugin_registry.__dict__)
                except Exception as e:
                    print(f"Error loading plugin {plugin_candidate}: {e}")
