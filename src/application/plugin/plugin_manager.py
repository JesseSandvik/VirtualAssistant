from src.domain import IPluginLoader, IPluginRegistry, IPluginValidator


class PluginManager:

    def __init__(self, loader: IPluginLoader, registry: IPluginRegistry, validator: IPluginValidator):
        self.loader = loader
        self.validator = validator
        self.registry = registry

    def load_plugins(self):
        self.loader.load_plugins()
        return self

    def register_plugins(self):
        for plugin in self.loader.plugins:
            self.validator.validate(plugin)
            self.registry.register_plugin(plugin)
            print(f"Plugin {plugin.instance.__class__.__name__} registered successfully.")
