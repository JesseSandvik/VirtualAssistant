import os
import unittest

from src.domain import PluginRegistry
from src.application import PluginManager
from src.infrastructure.plugin.plugin_loader import PluginLoader
from src.infrastructure.file_system.file_system import FileSystem


class TestPluginLoader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.plugin_manager = PluginManager(PluginRegistry())

    def test_load_plugins(self):
        project_root_directory = FileSystem.get_project_root_directory()
        plugins_test_directory = os.path.join(
            project_root_directory,
            "src",
            "infrastructure",
            "tests",
            "resources",
            "plugins"
        )
        PluginLoader(self.plugin_manager).load_plugins(plugins_test_directory)
        self.assertIn("FakePlugin", self.plugin_manager.registry.plugins)

