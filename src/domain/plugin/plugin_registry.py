from typing import Dict


class PluginRegistry:

    def __init__(self):
        self.plugins: Dict[str, object] = {}

    def register_plugin(self, plugin_name: str, plugin_instance: object):
        self.plugins[plugin_name] = plugin_instance

    def get_plugin(self, plugin_name: str) -> object:
        return self.plugins.get(plugin_name)
    
    def list_plugins(self) -> list:
        return list(self.plugins.keys())
