from dataclasses import dataclass

from src.domain.plugin import PluginMetadata

@dataclass
class FileSystemPluginMetadata(PluginMetadata):
    plugin_file_path: str

    def __init__(
        self,
        name: str,
        description: str,
        version: str,
        author_name: str,
        author_email: str,
        plugin_file_path: str
    ):
        super().__init__(name, description, version, author_name, author_email)
        self.plugin_file_path = plugin_file_path
