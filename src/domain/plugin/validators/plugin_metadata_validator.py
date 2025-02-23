from src.domain.plugin.validators.plugin_validator_interface import IPluginValidator
from src.domain.plugin.models.plugin import Plugin, PluginMetadata


class PluginMetadataValidator(IPluginValidator):

    def _check(self, plugin: Plugin):
        if not isinstance(plugin.metadata, PluginMetadata):
            raise ValueError("Plugin metadata must be an instance of PluginMetadata")
