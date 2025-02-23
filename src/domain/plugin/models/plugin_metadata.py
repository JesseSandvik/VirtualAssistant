from dataclasses import dataclass
from typing import List, Optional


@dataclass
class PluginMetadata:
    name: str
    description: str
    version: str
    author_name: str
    author_email: str
    enabled: bool
    keywords: Optional[List[str]] = None
