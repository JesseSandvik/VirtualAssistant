import unittest

from src.domain import PluginEntity, PluginMetadata, IPluginCore
from src.infrastructure import FileSystemPluginValidator


class MockValidPlugin(IPluginCore):
    pass


class MockInvalidPlugin:
    pass


class TestFileSystemPluginValidator(unittest.TestCase):

    def setUp(self):
        self.validator = FileSystemPluginValidator()

    def test_should_throw_exception_for_invalid_metadata_type_and_invalid_instance_type(self):
        invalid_plugin = PluginEntity(None, MockInvalidPlugin())
        try:
            self.validator.validate(invalid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertFalse(validation_passed)

    def test_should_throw_exception_for_valid_metadata_type_and_invalid_instance_type(self):
        valid_plugin = PluginEntity(PluginMetadata(
            name="test",
            description="test",
            version="test",
            author_name="Test Author",
            author_email="XXXXXXXXXXXXX",
            enabled=False
        ), MockInvalidPlugin())
        try:
            self.validator.validate(valid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertFalse(validation_passed)

    def test_should_throw_exception_for_invalid_metadata_type_and_valid_instance_type(self):
        valid_plugin = PluginEntity(None, MockValidPlugin())
        try:
            self.validator.validate(valid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertFalse(validation_passed)

    def test_should_not_throw_exception_for_valid_metadata_type_and_valid_instance_type(self):
        valid_plugin = PluginEntity(PluginMetadata(
            name="test",
            description="test",
            version="test",
            author_name="Test Author",
            author_email="XXXXXXXXXXXXX",
            enabled=False
        ), MockValidPlugin())
        try:
            self.validator.validate(valid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertTrue(validation_passed)
