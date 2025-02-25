import unittest

from unittest.mock import MagicMock

from src.domain import PluginMetadataEntity, PluginEntity, IPluginLoader, IPluginRegistry, IPluginValidator
from src.application import PluginManager


class MockPlugin:
    def __init__(self, name):
        self.instance = type(name, (), {})()


class TestPluginManager(unittest.TestCase):

    def setUp(self):
        self.mock_plugin_metadata = PluginMetadataEntity(
            name="Test Plugin",
            description="This is for testing purposes.",
            version="1.0.0",
            author_name="Walter White",
            author_email="XXXXXXXXXXXXXXXX"
        )
        self.mock_loader = MagicMock(spec=IPluginLoader)
        self.mock_registry = MagicMock(spec=IPluginRegistry)
        self.mock_validator = MagicMock(spec=IPluginValidator)
        self.plugin_manager = PluginManager(
            self.mock_loader, self.mock_registry, self.mock_validator
        )

    def test_load_plugins_should_call_plugin_loader_load_plugins(self):
        self.plugin_manager.load_plugins()
        self.mock_loader.load_plugins.assert_called_once()

    def test_register_plugins_should_call_validator_validate(self):
        mock_plugins = [
            PluginEntity(self.mock_plugin_metadata, instance=MockPlugin("PluginA"))
        ]
        self.mock_loader.plugins = mock_plugins
    
        self.plugin_manager.register_plugins()
        self.mock_validator.validate.assert_called_once_with(mock_plugins[0])

    def test_register_plugins_should_call_registry_register_plugin(self):
        mock_plugins = [
            PluginEntity(self.mock_plugin_metadata, instance=MockPlugin("PluginA"))
        ]
        self.mock_loader.plugins = mock_plugins
    
        self.plugin_manager.register_plugins()
        self.mock_registry.register_plugin.assert_called_once_with(mock_plugins[0])
