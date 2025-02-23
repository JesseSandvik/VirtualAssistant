from abc import ABC
from typing import Dict

from src.domain.plugin.models.plugin import Plugin


class IPluginRegistry(ABC):

    def __init__(self):
        self.registered_plugins: Dict[str, Plugin] = {}

    def get_plugin(self, plugin_name: str) -> Plugin:
        return self.registered_plugins.get(plugin_name)

    def register_plugin(self, plugin: Plugin) -> None:
        self.registered_plugins[plugin.instance.__class__.__name__] = plugin
