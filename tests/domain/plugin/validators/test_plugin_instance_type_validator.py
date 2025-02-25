import unittest

from src.domain import PluginMetadataEntity, PluginEntity, IPluginCore, PluginInstanceTypeValidator


class MockValidPlugin(IPluginCore):
    pass


class MockInvalidPlugin:
    pass


class TesPluginInstanceTypeValidator(unittest.TestCase):

    def setUp(self):
        self.mock_plugin_metadata = PluginMetadataEntity(
            name="Test Plugin",
            description="This is for testing purposes.",
            version="1.0.0",
            author_name="Walter White",
            author_email="XXXXXXXXXXXXXXXX"
        )
        self.validator = PluginInstanceTypeValidator()

    def test_should_not_throw_exception_for_valid_instance_type(self):
        valid_plugin = PluginEntity(self.mock_plugin_metadata, MockValidPlugin())
        try:
            self.validator.validate(valid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertTrue(validation_passed)

    def test_should_throw_exception_for_invalid_instance_type(self):
        invalid_plugin = PluginEntity(self.mock_plugin_metadata, MockInvalidPlugin())
        try:
            self.validator.validate(invalid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertFalse(validation_passed)
