import unittest

from src.domain.plugin import PluginCore, PluginCoreTypeValidator


class MockValidPlugin(PluginCore):
    pass


class MockInvalidPlugin:
    pass


class TesPluginCoreTypeValidator(unittest.TestCase):

    def setUp(self):
        self.validator = PluginCoreTypeValidator()

    def test_should_not_throw_exception_for_valid_instance_type(self):
        try:
            self.validator.validate(MockValidPlugin())
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertTrue(validation_passed)

    def test_should_throw_exception_for_invalid_instance_type(self):
        try:
            self.validator.validate(MockInvalidPlugin())
            validation_passed = True
        except Exception as e:
            validation_passed = False

        self.assertFalse(validation_passed)
