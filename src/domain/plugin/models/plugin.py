from dataclasses import dataclass

from src.domain.plugin.plugin_core_interface import IPluginCore
from src.domain.plugin.models.plugin_metadata import PluginMetadata


@dataclass
class Plugin:
    metadata: PluginMetadata
    instance: IPluginCore
