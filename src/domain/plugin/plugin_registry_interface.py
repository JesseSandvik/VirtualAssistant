from abc import ABC
from typing import Dict

from src.domain.plugin.entities.plugin_entity import PluginEntity


class IPluginRegistry(ABC):

    def __init__(self):
        self.registered_plugins: Dict[str, PluginEntity] = {}

    def get_plugin(self, plugin_name: str) -> PluginEntity:
        return self.registered_plugins.get(plugin_name)

    def register_plugin(self, plugin: PluginEntity) -> None:
        self.registered_plugins[plugin.instance.__class__.__name__] = plugin
