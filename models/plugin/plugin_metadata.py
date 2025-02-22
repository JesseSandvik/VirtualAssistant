from dataclasses import dataclass
from typing import List, Optional

from models.plugin.plugin_dependency import PluginDependency
from models.plugin.plugin_runtime import PluginRuntime


@dataclass
class PluginMetadata:
    name: str
    alias: str
    creator: str
    runtime: PluginRuntime
    repository: str
    description: str
    version: str
    requirements: Optional[List[PluginDependency]]
