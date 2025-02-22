from dataclasses import dataclass
from typing import List, Optional


@dataclass
class PluginRuntime:
    main: str
    tests: Optional[List[str]]
