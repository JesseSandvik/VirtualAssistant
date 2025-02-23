from src.domain import PluginRegistry


class PluginManager:

    def __init__(self, registry: PluginRegistry):
        self.registry = registry

    @staticmethod
    def __plugin_is_valid(plugin: object):
        # validate plugin
        return True

    def register_plugin(self, plugin_name: str, plugin_instance: object):
        if PluginManager.__plugin_is_valid(plugin_instance):
            self.registry.register_plugin(plugin_name, plugin_instance)
            print(f"Plugin {plugin_name} registered successfully.")
