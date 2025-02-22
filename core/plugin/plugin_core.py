from typing import Optional

from core.plugin.plugin_registry import PluginRegistry
from models.plugin import PluginDevice
from models.plugin import PluginMetadata


class PluginCore(object, metaclass = PluginRegistry):
    metadata = Optional[PluginMetadata]

    def __init__(self):
        pass

    def invoke(self, *args) -> PluginDevice:
        pass
