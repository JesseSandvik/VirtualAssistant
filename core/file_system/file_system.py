import os
import yaml

from enum import Enum


class FileSystemConfiguration(Enum):
    PROJECT_NAME = 'VirtualAssistant'
    CONFIGURATION_DIRECTORY = 'settings'
    PLUGINS_DIRECTORY = 'plugins'
    CONFIGURATION_FILE_NAME = 'configuration.yaml'


class FileSystem:

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
    def load_configuration(file_name: str = FileSystemConfiguration.CONFIGURATION_FILE_NAME.value):
        configuration_directory = FileSystem.get_configuration_directory()
        with open(os.path.join(configuration_directory, file_name)) as configuration_file:
            input_data = yaml.safe_load(configuration_file)
        return input_data
