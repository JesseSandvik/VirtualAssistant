import hashlib

from src.domain import PluginMetadataHasher


class PluginMetadataSHA256Hasher(PluginMetadataHasher):

    def calculate_hash(self, data: bytes):
        return hashlib.sha256(data).hexdigest()
    
    def verify_hash(self, data: bytes, expected_hash: str) -> bool:
        calculated_hash = self.calculate_hash(data)
        return calculated_hash == expected_hash
