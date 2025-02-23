from src.domain.plugin.validators.plugin_validator_interface import PluginValidatorInterface
from src.domain.plugin.plugin_core_interface import PluginCoreInterface
from src.domain.plugin.models.plugin import Plugin


class PluginInstanceTypeValidator(PluginValidatorInterface):

    def _check(self, plugin: Plugin):
        if not isinstance(plugin.instance, PluginCoreInterface):
            raise TypeError(f"Plugin {plugin.instance.__class__.__name__} must inherit from the base class PluginCoreInterface")
