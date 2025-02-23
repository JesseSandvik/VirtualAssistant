from src.domain import IPluginValidator, PluginInstanceTypeValidator, PluginMetadataValidator


class FileSystemPluginValidator(IPluginValidator):

    def validate(self, plugin):
        PluginInstanceTypeValidator(PluginMetadataValidator()).validate(plugin)
