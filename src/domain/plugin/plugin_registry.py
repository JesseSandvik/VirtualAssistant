from typing import Dict


class PluginRegistry:

    def __init__(self):
        self.plugins: Dict[str, object] = {}

    def register_plugin(self, plugin_name: str, plugin_instance: object):
        self.plugins[plugin_name] = plugin_instance

    def get_plugin(self, plugin_name: str) -> object:
        return self.plugins.get(plugin_name)
    
    def get_all_plugins(self) -> Dict[str, object]:
        return self.plugins
