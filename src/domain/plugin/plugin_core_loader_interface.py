from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.plugin.plugin_core_interface import IPluginCore


class IPluginCoreLoader(ABC):

    @abstractmethod
    def load(self) -> Optional[List[IPluginCore]]:
        pass
