from src.domain.plugin.validators.plugin_instance_type_validator import PluginInstanceTypeValidator
from src.domain.plugin.validators.plugin_metadata_validator import PluginMetadataValidator


class PluginValidator:

    @staticmethod
    def validate(plugin):
        PluginInstanceTypeValidator(PluginMetadataValidator()).validate(plugin)
