from src.domain import PluginMetadata, PluginMetadataValidator, PluginMetadataTypeValidator


class FileSystemPluginMetadataValidator(PluginMetadataValidator):

    def validate(self, plugin_metdata: PluginMetadata):
        PluginMetadataTypeValidator().validate(plugin_metdata)
