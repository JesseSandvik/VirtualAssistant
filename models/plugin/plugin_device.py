from dataclasses import dataclass
from typing import List


class PluginDevice:
    name: str
    firmware_version: str
    protocol: str
    errors: List[str]
