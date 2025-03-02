import os
import unittest

from virtual_assistant.infrastructure.file_system.plugin.file_system_plugin_service import FileSystemPluginService

class TestFileSystemPluginService(unittest.TestCase):

    def test_get_project_root_directory(self):
        project_root_directory = FileSystemPluginService().get_project_root_directory()
        self.assertEqual(project_root_directory, os.getcwd())
