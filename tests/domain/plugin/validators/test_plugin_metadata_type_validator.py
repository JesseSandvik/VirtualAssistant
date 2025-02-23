import unittest

from src.domain import Plugin, PluginMetadata, PluginMetadataTypeValidator


class TesPluginMetadataTypeValidator(unittest.TestCase):

    def setUp(self):
        self.validator = PluginMetadataTypeValidator()

    def test_should_not_throw_exception_for_valid_metadata_type(self):
        valid_plugin = Plugin(PluginMetadata(
            name="test",
            description="test",
            version="test",
            author_name="Test Author",
            author_email="XXXXXXXXXXXXX",
            enabled=False
        ), None)
        try:
            self.validator.validate(valid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertTrue(validation_passed)

    def test_should_throw_exception_for_invalid_metadata_type(self):
        invalid_plugin = Plugin(None, None)
        try:
            self.validator.validate(invalid_plugin)
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertFalse(validation_passed)
