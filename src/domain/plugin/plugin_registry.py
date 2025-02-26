from abc import ABC
from typing import Dict

from src.domain.plugin.plugin import Plugin


class PluginRegistry(ABC):

    def __init__(self):
        self.plugins: Dict[str, Plugin] = {}

    def get_plugin(self, plugin_id: str) -> Plugin:
        return self.plugins.get(plugin_id)

    def register_plugin(self, plugin: Plugin) -> None:
        self.plugins[plugin.plugin_id] = plugin
