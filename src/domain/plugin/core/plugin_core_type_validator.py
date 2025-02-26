from src.domain.plugin.plugin_validator_handler import PluginValidatorHandler
from src.domain.plugin.core.plugin_core import PluginCore


class PluginCoreTypeValidator(PluginValidatorHandler):

    def _check(self, plugin_core: PluginCore):
        if not isinstance(plugin_core, PluginCore):
            raise TypeError(f"Plugin {plugin_core.__class__.__name__} must inherit from the base class {PluginCore.__class__.__name__}")
