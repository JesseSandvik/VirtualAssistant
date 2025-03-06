import os
import unittest

from virtual_assistant.infrastructure.file_system.plugin.metadata.file_system_plugin_metadata_repository import FileSystemPluginMetadataRepository

class TestFileSystemPluginMetadataRepository(unittest.TestCase):

    def setUp(self):
        repository_test_file_path = os.path.join(
            os.getcwd(),
            'tests',
            'infrastructure',
            'file_system',
            'plugin',
            'resources',
            'test_repository.json'
        )
        self.plugin_metadata_repository = FileSystemPluginMetadataRepository(repository_test_file_path)

    def test_get_plugin_metadata(self):
        pass