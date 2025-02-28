from src.domain import PluginValidatorHandler
from src.domain import PluginMetadata


class PluginMetadataTypeValidator(PluginValidatorHandler):

    def _check(self, plugin_metadata: PluginMetadata):
        if not isinstance(plugin_metadata, PluginMetadata):
            raise ValueError("Plugin metadata must be an instance of PluginMetadata")
