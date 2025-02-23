import os
import yaml

from enum import Enum


class FileSystemConfiguration(Enum):
    PROJECT_NAME = 'VirtualAssistant'
    PROJECT_CONFIGURATION_FILE_NAME = 'application.yaml'
    CONFIGURATION_DIRECTORY = 'config'
    PLUGINS_DIRECTORY = 'plugins'
    PLUGIN_CONFIGUATION_FILE_NAME = 'plugin.yaml'


class FileSystem:

    @staticmethod
    def get_file_name_from_path(file_path: str) -> str:
        return os.path.basename(file_path)
    
    @staticmethod
    def remove_file_extension(file: str) -> str:
        return os.path.splitext(file)[0]
    
    @staticmethod
    def get_path_sections(path: str):
        return path.lstrip(os.sep).split(os.sep)
    
    @staticmethod
    def get_file_name_from_path_without_extension(file_path: str) -> str:
        return FileSystem.remove_file_extension(FileSystem.get_file_name_from_path(file_path))
    
    @staticmethod
    def get_file_path_after_root_directory(file_path: str) -> str:
        return file_path[file_path.find(FileSystemConfiguration.PROJECT_NAME.value) + len(FileSystemConfiguration.PROJECT_NAME.value) + 1:]

    @staticmethod
    def get_project_root_directory() -> str:
        current_directory = os.getcwd()
        return current_directory[0:current_directory.find(
            FileSystemConfiguration.PROJECT_NAME.value) + len(FileSystemConfiguration.PROJECT_NAME.value)]

    @staticmethod
    def get_configuration_directory() -> str:
        project_root_directory = FileSystem.get_project_root_directory()
        return os.path.join(project_root_directory, FileSystemConfiguration.CONFIGURATION_DIRECTORY.value)
    
    @staticmethod
    def get_plugins_directory() -> str:
        project_root_directory = FileSystem.get_project_root_directory()
        return os.path.join(project_root_directory, FileSystemConfiguration.PLUGINS_DIRECTORY.value)

    @staticmethod
    def load_configuration(configuration_file_path: str):
        with open(configuration_file_path) as configuration_file:
            configuration_file_content = yaml.safe_load(configuration_file)
        return configuration_file_content
