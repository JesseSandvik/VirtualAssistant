from src.domain.plugin.models.plugin import Plugin

from typing import Dict


class PluginRegistry:

    def __init__(self):
        self.plugins: Dict[str, Plugin] = {}

    def register_plugin(self, plugin: Plugin):
        self.plugins[plugin.instance.__class__.__name__] = plugin

    def get_plugin(self, plugin_name: str) -> Plugin:
        return self.plugins.get(plugin_name)
    
    def get_all_plugins(self) -> Dict[str, Plugin]:
        return self.plugins
