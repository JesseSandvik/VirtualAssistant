from dataclasses import dataclass


@dataclass
class PluginMetadata:
    name: str
    description: str
    version: str
    author_name: str
    author_email: str
    enabled: bool
