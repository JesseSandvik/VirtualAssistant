from src.domain.plugin.validators.plugin_validator_handler_interface import IPluginValidatorHandler
from src.domain.plugin.models.plugin import Plugin, PluginMetadata


class PluginMetadataValidator(IPluginValidatorHandler):

    def _check(self, plugin: Plugin):
        if not isinstance(plugin.metadata, PluginMetadata):
            raise ValueError("Plugin metadata must be an instance of PluginMetadata")
