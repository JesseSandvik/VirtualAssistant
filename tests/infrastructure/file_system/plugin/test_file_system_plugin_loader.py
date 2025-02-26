import os
import unittest

from src.infrastructure.file_system.plugin.core.file_system_plugin_core_loader import FileSystemPluginLoader
from src.infrastructure.file_system.file_system import FileSystem


class TestFileSystemPluginLoader(unittest.TestCase):

    def test_should_load_valid_plugin(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "tests",
            "infrastructure",
            'file_system',
            "resources",
            "plugins",
            "test-plugin-a"
        )
        loader = FileSystemPluginLoader(plugins_test_directory)
        loader.load_plugins()
        self.assertEqual("FakePluginA", loader.plugins[0].instance.__class__.__name__)

    def test_should_not_load_plugin_missing_plugin_configuration_file(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "tests",
            "infrastructure",
            'file_system',
            "resources",
            "plugins",
            "test-plugin-b"
        )
        loader = FileSystemPluginLoader(plugins_test_directory)
        loader.load_plugins()
        self.assertListEqual([], loader.plugins)

    def test_should_not_load_plugin_with_empty_plugin_configuration_file(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "tests",
            "infrastructure",
            'file_system',
            "resources",
            "plugins",
            "test-plugin-c"
        )
        loader = FileSystemPluginLoader(plugins_test_directory)
        loader.load_plugins()
        self.assertListEqual([], loader.plugins)

    def test_should_not_load_plugin_that_is_disabled(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "tests",
            "infrastructure",
            'file_system',
            "resources",
            "plugins",
            "test-plugin-d"
        )
        loader = FileSystemPluginLoader(plugins_test_directory)
        loader.load_plugins()
        self.assertListEqual([], loader.plugins)

    def test_should_not_load_plugin_file_that_is_empty(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "tests",
            "infrastructure",
            'file_system',
            "resources",
            "plugins",
            "test-plugin-e"
        )
        loader = FileSystemPluginLoader(plugins_test_directory)
        loader.load_plugins()
        self.assertListEqual([], loader.plugins)
