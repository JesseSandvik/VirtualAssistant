from dataclasses import dataclass
from uuid import uuid4

from src.domain.plugin.plugin_core_interface import IPluginCore
from src.domain.plugin.models.plugin_metadata import PluginMetadata


@dataclass
class PluginEntity:
    plugin_id: str
    metadata: PluginMetadata
    instance: IPluginCore
    is_active: bool

    def __init__(self, metadata: PluginMetadata, instance: IPluginCore):
        self.plugin_id = str(uuid4())
        self.metadata = metadata
        self.instance = instance
        self.is_active = False

    def activate(self):
        if not self.is_active:
            self.is_active = True
        else:
            raise ValueError(f"Plugin {self.name} is already active.")

    def deactivate(self):
        if self.is_active:
            self.is_active = False
        else:
            raise ValueError(f"Plugin {self.name} is already inactive.")
