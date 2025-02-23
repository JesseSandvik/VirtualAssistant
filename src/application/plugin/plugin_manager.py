from src.domain import Plugin, PluginRegistry, PluginValidator


class PluginManager:

    def __init__(self, registry: PluginRegistry):
        self.registry = registry

    def register_plugin(self, plugin: Plugin):
        PluginValidator.validate(plugin)
        self.registry.register_plugin(plugin)
        print(f"Plugin {plugin.instance.__class__.__name__} registered successfully.")
