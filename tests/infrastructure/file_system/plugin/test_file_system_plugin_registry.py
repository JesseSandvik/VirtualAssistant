import unittest

from src.domain import PluginEntity, IPluginCore
from src.infrastructure import FileSystemPluginRegistry


class MockPluginInstance(IPluginCore):
    pass


class TestFileSystemPluginRegistry(unittest.TestCase):

    def setUp(self):
        self.registry = FileSystemPluginRegistry()

    def test_should_get_plugin_from_registry(self):
        expected = PluginEntity(None, MockPluginInstance())
        self.registry.registered_plugins['MockPluginInstance'] = expected
        actual = self.registry.get_plugin('MockPluginInstance')

        self.assertEqual(actual, expected)

    def test_should_add_plugin_to_registry(self):
        plugin = PluginEntity(None, MockPluginInstance())
        self.registry.register_plugin(plugin)
        self.assertEqual(self.registry.registered_plugins.get('MockPluginInstance'), plugin)
