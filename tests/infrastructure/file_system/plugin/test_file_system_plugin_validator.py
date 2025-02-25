import unittest

from src.domain import PluginMetadataEntity, PluginEntity, IPluginCore
from src.infrastructure import FileSystemPluginValidator


class MockInvalidPluginMetadataType:

    def __init__(self):
        self.plugin_id = "XXXX"


class MockValidPlugin(IPluginCore):
    pass


class MockInvalidPlugin:
    pass


class TestFileSystemPluginValidator(unittest.TestCase):

    def setUp(self):
        self.mock_plugin_metadata = PluginMetadataEntity(
            name="Test Plugin",
            description="This is for testing purposes.",
            version="1.0.0",
            author_name="Walter White",
            author_email="XXXXXXXXXXXXXXXX"
        )
        self.validator = FileSystemPluginValidator()

    def test_should_throw_exception_for_invalid_metadata_type_and_invalid_instance_type(self):
        invalid_plugin = PluginEntity(MockInvalidPluginMetadataType(), MockInvalidPlugin())
        try:
            self.validator.validate(invalid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertFalse(validation_passed)

    def test_should_throw_exception_for_valid_metadata_type_and_invalid_instance_type(self):
        valid_plugin = PluginEntity(self.mock_plugin_metadata, MockInvalidPlugin())
        try:
            self.validator.validate(valid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertFalse(validation_passed)

    def test_should_throw_exception_for_invalid_metadata_type_and_valid_instance_type(self):
        valid_plugin = PluginEntity(MockInvalidPluginMetadataType(), MockValidPlugin())
        try:
            self.validator.validate(valid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertFalse(validation_passed)

    def test_should_not_throw_exception_for_valid_metadata_type_and_valid_instance_type(self):
        valid_plugin = PluginEntity(self.mock_plugin_metadata, MockValidPlugin())
        try:
            self.validator.validate(valid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertTrue(validation_passed)
