from dataclasses import dataclass

from src.domain.plugin.plugin_core_interface import PluginCoreInterface
from src.domain.plugin.models.plugin_metadata import PluginMetadata

@dataclass
class Plugin:
    metadata: PluginMetadata
    instance: PluginCoreInterface
