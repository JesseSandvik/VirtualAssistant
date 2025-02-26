from src.domain.plugin.validators.plugin_validator_handler_interface import IPluginValidatorHandler
from src.domain.plugin.plugin_core_interface import IPluginCore


class PluginCoreTypeValidator(IPluginValidatorHandler):

    def _check(self, plugin_core: IPluginCore):
        if not isinstance(plugin_core, IPluginCore):
            raise TypeError(f"Plugin {plugin_core.__class__.__name__} must inherit from the base class {IPluginCore.__class__.__name__}")
