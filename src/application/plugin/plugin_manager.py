from src.domain import Plugin, PluginLoader, PluginRegistry, PluginValidator


class PluginManager:

    def __init__(self, loader: PluginLoader, registry: PluginRegistry, validator: PluginValidator):
        self.loader = loader
        self.registry = registry
        self.validator = validator

    def load_plugins(self):
        self.loader.load_plugins()

    def register_plugin(self, plugin: Plugin):
        self.validator.validate(plugin)
        self.registry.register_plugin(plugin)
        print(f"Plugin {plugin.instance.__class__.__name__} registered successfully.")
