from src.domain import PluginCoreLoader, PluginCoreValidator


class PluginCoreManager:

    def __init__(self, loader: PluginCoreLoader, validator: PluginCoreValidator):
        self.loader = loader
        self.validator = validator

    def load_plugin_cores(self):
        self.loader.load()
        return self
    
    def validate_plugin_cores(self):
        for plugin_core in self.loader.plugin_cores:
            self.validator.validate(plugin_core)
        return self
