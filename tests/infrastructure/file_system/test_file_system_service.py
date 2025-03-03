import os
import unittest

from virtual_assistant.infrastructure.file_system.file_system_service import FileSystemService

class TestFileSystemService(unittest.TestCase):

    def test_get_json_file_content(self):
        json_file_path = os.path.join(
            os.getcwd(),
            'tests',
            'infrastructure',
            'file_system',
            'resources',
            'test.json'
        )
        json_file_content = FileSystemService.get_json_file_content(json_file_path)
        self.assertEqual(json_file_content['keyA'], 'valueA')

    def test_get_yaml_file_content(self):
        yaml_file_path = os.path.join(
            os.getcwd(),
            'tests',
            'infrastructure',
            'file_system',
            'resources',
            'test.yaml'
        )
        yaml_file_content = FileSystemService.get_yaml_file_contents(yaml_file_path)
        self.assertEqual(yaml_file_content['first_key'], 'value 1')
