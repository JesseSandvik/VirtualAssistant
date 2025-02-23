import os
import unittest

from src.domain import PluginRegistry
from src.application import PluginManager
from src.infrastructure.plugin.plugin_loader import PluginLoader
from src.infrastructure.file_system.file_system import FileSystem


class TestPluginLoader(unittest.TestCase):

    def setUp(self):
        self.plugin_manager = PluginManager(PluginRegistry())

    def test_should_load_valid_plugin(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "src",
            "infrastructure",
            "tests",
            "resources",
            "plugins",
            "test-plugin-a"
        )
        PluginLoader(self.plugin_manager).load_plugins(plugins_test_directory)
        self.assertIn("FakePluginA", self.plugin_manager.registry.plugins)

    def test_should_not_load_plugin_missing_plugin_configuration_file(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "src",
            "infrastructure",
            "tests",
            "resources",
            "plugins",
            "test-plugin-b"
        )
        PluginLoader(self.plugin_manager).load_plugins(plugins_test_directory)
        self.assertDictEqual({}, self.plugin_manager.registry.plugins)

    def test_should_not_load_plugin_with_empty_plugin_configuration_file(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "src",
            "infrastructure",
            "tests",
            "resources",
            "plugins",
            "test-plugin-c"
        )
        PluginLoader(self.plugin_manager).load_plugins(plugins_test_directory)
        self.assertDictEqual({}, self.plugin_manager.registry.plugins)

    def test_should_not_load_plugin_that_is_disabled(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "src",
            "infrastructure",
            "tests",
            "resources",
            "plugins",
            "test-plugin-d"
        )
        PluginLoader(self.plugin_manager).load_plugins(plugins_test_directory)
        self.assertDictEqual({}, self.plugin_manager.registry.plugins)

    def test_should_not_load_plugin_that_is_not_an_instance_of_plugin_core(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "src",
            "infrastructure",
            "tests",
            "resources",
            "plugins",
            "test-plugin-e"
        )
        PluginLoader(self.plugin_manager).load_plugins(plugins_test_directory)
        self.assertDictEqual({}, self.plugin_manager.registry.plugins)

    def test_should_not_load_plugin_file_that_is_empty(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "src",
            "infrastructure",
            "tests",
            "resources",
            "plugins",
            "test-plugin-f"
        )
        PluginLoader(self.plugin_manager).load_plugins(plugins_test_directory)
        self.assertDictEqual({}, self.plugin_manager.registry.plugins)
