import unittest

from src.domain import PluginMetadataEntity, PluginEntity, IPluginCore
from src.infrastructure import FileSystemPluginRegistry


class MockPluginInstance(IPluginCore):
    pass


class TestFileSystemPluginRegistry(unittest.TestCase):

    def setUp(self):
        self.mock_plugin_metadata = PluginMetadataEntity(
            name="Test Plugin",
            description="This is for testing purposes.",
            version="1.0.0",
            author_name="Walter White",
            author_email="XXXXXXXXXXXXXXXX"
        )
        self.registry = FileSystemPluginRegistry()

    def test_should_get_plugin_from_registry(self):
        expected = PluginEntity(self.mock_plugin_metadata, MockPluginInstance())
        self.registry.registered_plugins[expected.plugin_id] = expected
        actual = self.registry.get_plugin(expected.plugin_id)
        self.assertEqual(actual, expected)

    def test_should_add_plugin_to_registry(self):
        plugin = PluginEntity(self.mock_plugin_metadata, MockPluginInstance())
        self.registry.register_plugin(plugin)
        self.assertEqual(self.registry.registered_plugins.get(plugin.plugin_id), plugin)
