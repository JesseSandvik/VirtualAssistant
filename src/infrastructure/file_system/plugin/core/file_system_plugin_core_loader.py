# import inspect
# import os

# from importlib import import_module
# from typing import List

# from src.domain.plugin.core import PluginCoreLoader
# from src.domain.plugin.metadata import PluginMetadata
# from src.domain.plugin import Plugin
# from src.infrastructure.file_system import FileSystem, FileSystemConfiguration


# class FileSystemPluginLoader(PluginCoreLoader):
#     __IGNORE_DIRECTORIES = ['__pycache__']
#     __IGNORE_FILES = ['__init__.py']

#     def __init__(self, plugins_directory: str = FileSystem.get_plugins_directory()):
#         self.plugins: List[Plugin] = []
#         self.plugins_directory = plugins_directory

#     def __discover_plugin_paths(self) -> List[str]:
#         plugin_paths = []
#         for root, dirs, files in os.walk(self.plugins_directory):
#             dirs[:] = [d for d in dirs if d not in FileSystemPluginLoader.__IGNORE_DIRECTORIES]

#             for file in files:
#                 if file.endswith(".py") and file not in FileSystemPluginLoader.__IGNORE_FILES:
#                     plugin_paths.append(os.path.join(root, file))

#         return plugin_paths

#     def __get_plugin_configuration_from_plugin_file_path(self, plugin_file_path: str):
#         try:
#             plugin_candidate_entry_point = FileSystem.get_file_name_from_path(plugin_file_path)
#             plugin_candidate_configuration_file_path = plugin_file_path.replace(plugin_candidate_entry_point, FileSystemConfiguration.PLUGIN_CONFIGUATION_FILE_NAME.value)
#             return FileSystem.load_configuration(plugin_candidate_configuration_file_path)
#         except FileNotFoundError as e:
#             print(f"Error loading plugin configuration for {plugin_file_path}: {e}")
#             return {}

#     def __get_plugin_module_from_plugin_file_path(self, plugin_file_path: str):
#         plugin_module_path = FileSystem.get_file_path_after_root_directory(plugin_file_path)
#         plugin_module_path_without_file_extension = FileSystem.remove_file_extension(plugin_module_path)
#         plugin_module_import_path = '.'.join(FileSystem.get_path_sections(plugin_module_path_without_file_extension))
#         return import_module(plugin_module_import_path)
    
#     def __load_plugin(self, plugin_module, plugin_configuration):
#         for plugin_class_name, plugin_class in inspect.getmembers(plugin_module, inspect.isclass):
#             if plugin_class.__module__ == plugin_module.__name__:
#                 plugin_metadata = PluginMetadata(
#                     name=plugin_configuration.get('name'),
#                     description=plugin_configuration.get('description'),
#                     version=plugin_configuration.get('version'),
#                     author_name=plugin_configuration.get('author_name'),
#                     author_email=plugin_configuration.get('author_email')
#                 )
#                 self.plugins.append(Plugin(plugin_metadata, plugin_class()))

#     def load_plugins(self) -> List[str]:
#         plugin_candidate_file_paths = self.__discover_plugin_paths()

#         for plugin_candidate_file_path in plugin_candidate_file_paths:
#             plugin_candidate_configuration = self.__get_plugin_configuration_from_plugin_file_path(plugin_candidate_file_path)

#             if not plugin_candidate_configuration:
#                 print(f"no plugin configuration found for {plugin_candidate_file_path}")
#                 print(f"please make sure: {plugin_candidate_file_path} has a valid {FileSystemConfiguration.PLUGIN_CONFIGUATION_FILE_NAME.value} file")
#                 continue

#             if plugin_candidate_configuration.get('enabled', False):
#                 try:
#                     plugin_module = self.__get_plugin_module_from_plugin_file_path(plugin_candidate_file_path)
#                     self.__load_plugin(plugin_module, plugin_candidate_configuration)

#                 except Exception as e:
#                     print(f"Error loading plugin {plugin_candidate_file_path}: {e}")
#             else:
#                 print(f"plugin {plugin_candidate_file_path} found, but is disabled in plugin configuration file: {FileSystemConfiguration.PLUGIN_CONFIGUATION_FILE_NAME.value}")
