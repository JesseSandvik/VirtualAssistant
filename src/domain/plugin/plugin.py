from dataclasses import dataclass

from src.domain.plugin.core.plugin_core import PluginCore
from src.domain.plugin.metadata.plugin_metadata import PluginMetadata


@dataclass
class Plugin:
    id: str
    metadata: PluginMetadata
    core: PluginCore

    def __init__(self, plugin_metadata: PluginMetadata, plugin_core: PluginCore):
        self.id = plugin_metadata.plugin_id
        self.metadata = plugin_metadata
        self.core = plugin_core
