from src.domain.plugin.validators.plugin_validator_interface import IPluginValidator
from src.domain.plugin.plugin_core_interface import IPluginCore
from src.domain.plugin.models.plugin import Plugin


class PluginInstanceTypeValidator(IPluginValidator):

    def _check(self, plugin: Plugin):
        if not isinstance(plugin.instance, IPluginCore):
            raise TypeError(f"Plugin {plugin.instance.__class__.__name__} must inherit from the base class PluginCoreInterface")
