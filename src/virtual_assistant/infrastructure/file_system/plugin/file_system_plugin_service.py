import os

from enum import Enum

from virtual_assistant.infrastructure.file_system.file_system_service import FileSystemService

class FileSystemPluginSettings(Enum):
    PROJECT_ROOT_DIRECTORY_NAME='virtual_assistant'
    DEFAULT_PLUGIN_CONFIGURATION_FILE_NAME = 'plugin.yaml'

class FileSystemPluginService(FileSystemService):

    @staticmethod
    def get_project_root_directory() -> str:
        current_directory = os.getcwd()
        return current_directory[0:current_directory.find(
            FileSystemPluginSettings.PROJECT_ROOT_DIRECTORY_NAME.value) + 
                len(FileSystemPluginSettings.PROJECT_ROOT_DIRECTORY_NAME.value)]
