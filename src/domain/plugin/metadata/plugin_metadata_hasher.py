from abc import ABC, abstractmethod


class PluginMetadataHasher(ABC):

    @abstractmethod
    def calculate_hash(self, data: bytes) -> str:
        pass

    @abstractmethod
    def verify_hash(self, data: bytes, expected_hash: str) -> bool:
        pass
