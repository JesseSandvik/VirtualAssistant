from src.domain import IPluginValidator, PluginInstanceTypeValidator, PluginMetadataTypeValidator


class FileSystemPluginValidator(IPluginValidator):

    def validate(self, plugin):
        PluginInstanceTypeValidator(PluginMetadataTypeValidator()).validate(plugin)
