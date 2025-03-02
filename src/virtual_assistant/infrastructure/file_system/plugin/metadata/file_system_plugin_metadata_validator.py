from virtual_assistant.domain.plugin.metadata.plugin_metadata import PluginMetadata
from virtual_assistant.domain.plugin.metadata.plugin_metadata_type_validator import PluginMetadataTypeValidator

from virtual_assistant.domain.plugin.metadata.plugin_metadata_validator import PluginMetadataValidator

class FileSystemPluginMetadataValidator(PluginMetadataValidator):
    
    def validate(self, plugin_metadata: PluginMetadata) -> None:
        PluginMetadataTypeValidator().validate(plugin_metadata)
