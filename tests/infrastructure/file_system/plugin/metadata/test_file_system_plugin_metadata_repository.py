import os
import unittest

from virtual_assistant.domain.plugin.metadata.plugin_metadata import PluginMetadata
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

    def test_create_plugin_metadata(self):
        new_plugin_metadata = PluginMetadata(
            entry_point='test_file.py',
            name='test_plugin',
            description='test_plugin_description',
            version='0.0.1',
            author='test_author',
            required_python_version='3.13.3',
            compatible_application_versions=['1.0.0']

        )
        self.plugin_metadata_repository.create_plugin_metadata(new_plugin_metadata)
        plugin_metadata_from_repository = self.plugin_metadata_repository.get_plugin_metadata_by_entry_point(new_plugin_metadata.entry_point)
        self.assertEqual(new_plugin_metadata.entry_point, plugin_metadata_from_repository.entry_point)