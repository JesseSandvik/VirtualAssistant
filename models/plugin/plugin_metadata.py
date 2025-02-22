from dataclasses import dataclass
from typing import Optional


@dataclass
class PluginMetadata:
    name: str
    version: str
    description: Optional[str]
    author: str
    license: Optional[str]
    url: Optional[str]
    tags: Optional[list[str]]
