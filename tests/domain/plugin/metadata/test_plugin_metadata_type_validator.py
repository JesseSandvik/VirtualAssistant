import unittest

from virtual_assistant.domain.plugin.metadata.plugin_metadata import PluginMetadata
from virtual_assistant.domain.plugin.metadata.plugin_metadata_type_validator import PluginMetadataTypeValidator

class MockInvalidPluginMetadataType:
    pass

class TesPluginMetadataTypeValidator(unittest.TestCase):

    def setUp(self):
        self.mock_plugin_metadata = PluginMetadata(
            entry_point='Mock Plugin',
            name='Mock Plugin',
            description='Mock Plugin Description',
            version='1.0.0',
            author='Mock Author',
            required_python_version='3.13.3'
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
