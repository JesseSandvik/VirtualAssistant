from src.domain.plugin.validators.plugin_validator_handler_interface import IPluginValidatorHandler
from src.domain.plugin.plugin_core_interface import IPluginCore
from src.domain.plugin.entities.plugin_entity import PluginEntity


class PluginInstanceTypeValidator(IPluginValidatorHandler):

    def _check(self, plugin: PluginEntity):
        if not isinstance(plugin.instance, IPluginCore):
            raise TypeError(f"Plugin {plugin.instance.__class__.__name__} must inherit from the base class PluginCoreInterface")
