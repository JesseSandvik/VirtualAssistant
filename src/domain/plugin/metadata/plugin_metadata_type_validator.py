from src.domain.plugin.plugin_validator_handler import PluginValidatorHandler
from src.domain.plugin.metadata.plugin_metadata import PluginMetadata


class PluginMetadataTypeValidator(PluginValidatorHandler):

    def _check(self, plugin_metadata: PluginMetadata):
        if not isinstance(plugin_metadata, PluginMetadata):
            raise ValueError("Plugin metadata must be an instance of PluginMetadata")
