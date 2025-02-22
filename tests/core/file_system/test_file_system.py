import unittest

from core.file_system import FileSystemConfiguration, FileSystem


class TestFileSystem(unittest.TestCase):

    def test_should_get_project_root_directory(self):
        project_root_directory = FileSystem.get_project_root_directory()
        self.assertIn(FileSystemConfiguration.PROJECT_NAME.value, project_root_directory)

    def test_should_get_configuration_directory(self):
        project_root_directory = FileSystem.get_configuration_directory()
        self.assertIn(FileSystemConfiguration.CONFIGURATION_DIRECTORY.value, project_root_directory)

    def test_should_get_plugins_directory(self):
        project_root_directory = FileSystem.get_plugins_directory()
        self.assertIn(FileSystemConfiguration.PLUGINS_DIRECTORY.value, project_root_directory)

    def test_should_load_configuration(self):
        configuration = FileSystem.load_configuration()
        self.assertTrue(configuration)
