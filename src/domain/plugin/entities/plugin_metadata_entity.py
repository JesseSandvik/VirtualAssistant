from dataclasses import dataclass
from datetime import datetime
from packaging.version import Version
from uuid import uuid4


@dataclass
class PluginMetadataEntity:
    plugin_id: str
    name: str
    description: str
    version: str
    author_name: str
    author_email: str
    last_updated: datetime
    is_valid: bool = False

    def __init__(
        self,
        name: str,
        description: str,
        version: str,
        author_name: str,
        author_email: str
    ):
        self.plugin_id = str(uuid4())
        self.name = name
        self.description = description
        self.version = version
        self.author_name = author_name
        self.author_email = author_email
        self.last_updated = datetime.now()

    def update(self, **args):
        for key, value in args.items():
            setattr(self, key, value)
            self.last_updated = datetime.now()

    def version_has_changed(self, version: str) -> bool:
        return Version(self.version) < Version(version)
