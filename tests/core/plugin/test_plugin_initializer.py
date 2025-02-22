import os
import unittest

from core.file_system import FileSystem
from core.plugin import PluginInitializer


class TestPluginInitializer(unittest.TestCase):
    __TEST_PLUGIN_DIRECTORY = os.path.join(
        FileSystem.get_project_root_directory(),
        'tests',
        'resources',
        'plugins'
    )

    @classmethod
    def setUpClass(cls):
        cls.plugin_initializer = PluginInitializer()

    def test_should_return_initialized_runtime_for_properly_configured_plugin_module(self):
        initialized_plugin_runtime = self.plugin_initializer.initialize(
            'test-plugin-a',
            plugin_directory=TestPluginInitializer.__TEST_PLUGIN_DIRECTORY
        )
        self.assertEqual(initialized_plugin_runtime, 'test_plugin_a.py')

    def test_should_return_none_for_non_existent_plugin_module(self):
        initialized_plugin_runtime = self.plugin_initializer.initialize(
            'non-existent',
            plugin_directory=TestPluginInitializer.__TEST_PLUGIN_DIRECTORY
        )
        self.assertIsNone(initialized_plugin_runtime)

    def test_should_return_none_for_plugin_module_with_no_configuration_file(self):
        initialized_plugin_runtime = self.plugin_initializer.initialize(
            'test-plugin-no-configuration',
            plugin_directory=TestPluginInitializer.__TEST_PLUGIN_DIRECTORY
        )
        self.assertIsNone(initialized_plugin_runtime)

    def test_should_return_none_for_plugin_module_with_empty_configuration_file(self):
        initialized_plugin_runtime = self.plugin_initializer.initialize(
            'test-plugin-empty-configuration',
            plugin_directory=TestPluginInitializer.__TEST_PLUGIN_DIRECTORY
        )
        self.assertIsNone(initialized_plugin_runtime)
