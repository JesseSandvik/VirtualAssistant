import os
import unittest

from src.infrastructure import FileSystem, FileSystemConfiguration


class TestFileSystem(unittest.TestCase):

    def test_should_get_file_name_from_path(self):
        file_name = FileSystem.get_file_name_from_path('/path/to/file.txt')
        self.assertEqual(file_name, 'file.txt')

    def test_should_remove_file_extension(self):
        file_name = FileSystem.remove_file_extension('/path/to/file.txt')
        self.assertEqual(file_name, '/path/to/file')

    def test_should_get_path_sections_with_leading_path_separator(self):
        path_sections = FileSystem.get_path_sections('/path/to/file.txt')
        self.assertEqual(path_sections[0], 'path')
        self.assertEqual(path_sections[1], 'to')
        self.assertEqual(path_sections[2], 'file.txt')

    def test_should_get_path_sections_without_leading_path_separator(self):
        path_sections = FileSystem.get_path_sections('path/to/file.txt')
        self.assertEqual(path_sections[0], 'path')
        self.assertEqual(path_sections[1], 'to')
        self.assertEqual(path_sections[2], 'file.txt')

    def test_should_get_file_name_from_path_without_extension(self):
        file_name = FileSystem.get_file_name_from_path_without_extension('/path/to/file.txt')
        self.assertEqual(file_name, 'file')

    def test_should_get_file_path_after_root_directory(self):
        file_path = FileSystem.get_file_path_after_root_directory(FileSystem.get_plugins_directory())
        self.assertEqual(file_path, FileSystemConfiguration.PLUGINS_DIRECTORY.value)

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
        configuration_file_path = os.path.join(
            FileSystem.get_configuration_directory(),
            FileSystemConfiguration.PROJECT_CONFIGURATION_FILE_NAME.value
        )
        configuration = FileSystem.load_configuration(configuration_file_path)
        self.assertTrue(configuration)
