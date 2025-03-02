from .plugin_metadata import PluginMetadata
from .plugin_metadata_base_validator import PluginMetadataBaseValidator

class PluginMetadataTypeValidator(PluginMetadataBaseValidator):

    def _check(self, plugin_metadata):
        if not isinstance(plugin_metadata, PluginMetadata):
            raise TypeError("Plugin metadata must be of type PluginMetadata")
