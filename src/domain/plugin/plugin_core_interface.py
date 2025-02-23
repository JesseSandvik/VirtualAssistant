from abc import ABC

from src.domain.plugin.plugin_registry import PluginRegistry


class PluginCoreInterface(ABC):

    def __init__(self, registry: PluginRegistry):
        self.registry = registry
        self.plugin_name = self.__class__.__name__
        self.registry.register_plugin(self.plugin_name, self)
