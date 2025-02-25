from dataclasses import dataclass

from src.domain.plugin.plugin_core_interface import IPluginCore
from src.domain.plugin.entities.plugin_metadata_entity import PluginMetadataEntity


@dataclass
class PluginEntity:
    plugin_id: str
    metadata: PluginMetadataEntity
    instance: IPluginCore

    def __init__(self, metadata: PluginMetadataEntity, instance: IPluginCore):
        self.plugin_id = metadata.plugin_id
        self.metadata = metadata
        self.instance = instance
