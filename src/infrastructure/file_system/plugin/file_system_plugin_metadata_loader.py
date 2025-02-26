from typing import List, Optional

from src.domain import PluginMetadataEntity, IPluginMetadataLoader


class FileSystemPluginMetadataLoader(IPluginMetadataLoader):

    def load(self) -> Optional[List[PluginMetadataEntity]]:
        # TODO: load plugin metadata from file system
        return []
