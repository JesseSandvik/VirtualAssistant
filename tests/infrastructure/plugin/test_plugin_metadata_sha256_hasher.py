import hashlib
import unittest

from src.infrastructure import PluginMetadataSHA256Hasher


class TestPluginMetadataSHA256Hasher(unittest.TestCase):

    def setUp(self):
        self.plugin_metadata_hasher = PluginMetadataSHA256Hasher()

    def test_calculate_hash(self):
        data = b"plugin_metadata_example"
        calculated_hash = self.plugin_metadata_hasher.calculate_hash(data)
        expected_hash = hashlib.sha256(data).hexdigest()
        self.assertEqual(calculated_hash, expected_hash)

    def test_verify_hash_is_correct(self):
        data = b"plugin_metadata_example"
        expected_hash = hashlib.sha256(data).hexdigest()
        result = self.plugin_metadata_hasher.verify_hash(data, expected_hash)
        self.assertTrue(result)

    def test_verify_hash_is_incorrect(self):
        data = b"plugin_metadata_example"
        incorrect_hash = "incorrect_hash_value"
        result = self.plugin_metadata_hasher.verify_hash(data, incorrect_hash)
        self.assertFalse(result)
