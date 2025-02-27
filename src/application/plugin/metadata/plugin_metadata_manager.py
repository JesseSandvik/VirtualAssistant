from src.domain.plugin import PluginMetadataLoader, PluginMetadataHasher, PluginCoreTypeValidator, PluginMetadataRepository


class PluginMetadataManager:

    def __init__(
            self,
            loader: PluginMetadataLoader,
            hasher: PluginMetadataHasher,
            validator: PluginCoreTypeValidator,
            repository: PluginMetadataRepository
        ):
        self.loader = loader
        self.hasher = hasher
        self.validator = validator
        self.repository = repository

    def load_plugin_metadata(self):
        self.loader.load()
        return self
    
    def validate_plugin_metadata(self):
        for plugin_metadata in self.loader.plugin_metadata:
            self.validator.validate(plugin_metadata)
        return self
    
    def hash_plugin_metadata(self):
        for plugin_metadata in self.loader.plugin_metadata:
            self.hasher.hash(plugin_metadata)
        return self
    
    def save_plugin_metadata(self):
        for plugin_metadata in self.loader.plugin_metadata:
            self.repository.save(plugin_metadata)
        return self
