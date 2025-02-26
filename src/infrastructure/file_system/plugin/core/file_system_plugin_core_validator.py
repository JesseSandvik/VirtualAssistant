from src.domain.plugin import PluginCore, PluginCoreValidator, PluginCoreTypeValidator


class FileSystemPluginCoreValidator(PluginCoreValidator):

    def validate(self, plugin_core: PluginCore):
        PluginCoreTypeValidator().validate(plugin_core)
