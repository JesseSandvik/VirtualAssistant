from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.plugin.core.plugin_core import PluginCore


class PluginCoreLoader(ABC):

    def __init__(self):
        self.plugin_cores = []

    @abstractmethod
    def load(self) -> Optional[List[PluginCore]]:
        pass
