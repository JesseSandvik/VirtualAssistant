from src.domain.plugin.validators.plugin_validator_handler_interface import IPluginValidatorHandler
from src.domain.plugin.entities.plugin_entity import PluginMetadataEntity, PluginEntity


class PluginMetadataTypeValidator(IPluginValidatorHandler):

    def _check(self, plugin: PluginEntity):
        if not isinstance(plugin.metadata, PluginMetadataEntity):
            raise ValueError("Plugin metadata must be an instance of PluginMetadata")
