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
        plugin_metadata = self.plugin_metadata_repository.get_plugin_metadata()
        self.assertEqual(plugin_metadata.name, 'virtual_assistant')
        self.assertEqual(plugin_metadata.version, '0.0.1')
        self.assertEqual(plugin_metadata.description, 'Virtual Assistant')
        self.assertEqual(plugin_metadata.author, 'Rafael')
        self.assertEqual(plugin_metadata.author_email, 'XXXXXXXXXXXXXXXXX')
        self.assertEqual(plugin_metadata.url, 'XXXXXXXXXXXXXXXXXXXXXXXXX')
        self.assertEqual(plugin_metadata.license, 'MIT')