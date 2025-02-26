from abc import ABC, abstractmethod
from typing import Optional, List

from src.domain.plugin.entities.plugin_metadata_entity import PluginMetadataEntity


class IPluginMetadataLoader(ABC):

    @abstractmethod
    def load(self) -> Optional[List[PluginMetadataEntity]]:
        pass
