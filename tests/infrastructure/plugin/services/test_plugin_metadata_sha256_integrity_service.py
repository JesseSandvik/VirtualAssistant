import hashlib
import unittest

from src.infrastructure import PluginMetadataSHA256IntegrityService


class TestPluginMetadataSHA256IntegrityService(unittest.TestCase):

    def setUp(self):
        self.integrity_service = PluginMetadataSHA256IntegrityService()

    def test_calculate_hash(self):
        data = b"plugin_metadata_example"
        calculated_hash = self.integrity_service.calculate_hash(data)
        expected_hash = hashlib.sha256(data).hexdigest()
        self.assertEqual(calculated_hash, expected_hash)

    def test_verify_hash_is_correct(self):
        data = b"plugin_metadata_example"
        expected_hash = hashlib.sha256(data).hexdigest()
        result = self.integrity_service.verify_hash(data, expected_hash)
        self.assertTrue(result)

    def test_verify_hash_is_incorrect(self):
        data = b"plugin_metadata_example"
        incorrect_hash = "incorrect_hash_value"
        result = self.integrity_service.verify_hash(data, incorrect_hash)
        self.assertFalse(result)
