from src.domain import PluginRegistry, PluginValidator


class PluginManager:

    def __init__(self, registry: PluginRegistry):
        self.registry = registry

    def register_plugin(self, plugin_name: str, plugin_instance: object):
        PluginValidator.validate(plugin_instance)
        self.registry.register_plugin(plugin_name, plugin_instance)
        print(f"Plugin {plugin_name} registered successfully.")
