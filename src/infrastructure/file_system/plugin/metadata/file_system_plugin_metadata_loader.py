from typing import List, Optional

from src.domain import PluginMetadata, PluginMetadataLoader


class FileSystemPluginMetadataLoader(PluginMetadataLoader):

    def load(self) -> Optional[List[PluginMetadata]]:
        # TODO: load plugin metadata from file system
        return []
