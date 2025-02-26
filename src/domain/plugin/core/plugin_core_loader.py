from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.plugin.core.plugin_core import PluginCore


class PluginCoreLoader(ABC):

    @abstractmethod
    def load(self) -> Optional[List[PluginCore]]:
        pass
