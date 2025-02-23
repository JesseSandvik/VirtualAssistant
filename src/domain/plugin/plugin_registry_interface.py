from abc import ABC
from typing import Dict

from src.domain.plugin.models.plugin import Plugin


class IPluginRegistry(ABC):

    def __init__(self):
        self.registry: Dict[str, Plugin] = {}

    def register_plugin(self, plugin: Plugin) -> None:
        self.registry[plugin.instance.__class__.__name__] = plugin

    def get_plugin(self, plugin_name: str) -> Plugin:
        return self.registry.get(plugin_name)
