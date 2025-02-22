from dataclasses import dataclass


@dataclass
class PluginDependency:
    name: str
    version: str
