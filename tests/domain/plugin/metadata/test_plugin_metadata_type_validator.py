import unittest

from src.domain.plugin import PluginMetadata, PluginMetadataTypeValidator


class MockInvalidPluginMetadataType:

    def __init__(self):
        self.plugin_id = "XXXX"


class TesPluginMetadataTypeValidator(unittest.TestCase):

    def setUp(self):
        self.mock_plugin_metadata = PluginMetadata(
            name="Test Plugin",
            description="This is for testing purposes.",
            version="1.0.0",
            author_name="Walter White",
            author_email="XXXXXXXXXXXXXXXX"
        )
        self.validator = PluginMetadataTypeValidator()

    def test_should_not_throw_exception_for_valid_metadata_type(self):
        try:
            self.validator.validate(self.mock_plugin_metadata)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertTrue(validation_passed)

    def test_should_throw_exception_for_invalid_metadata_type(self):
        try:
            self.validator.validate(MockInvalidPluginMetadataType())
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertFalse(validation_passed)
