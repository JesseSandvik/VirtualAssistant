from abc import ABC, abstractmethod


class IPluginMetadataLoader(ABC):

    @abstractmethod
    def load_plugin_metadata(self):
        pass
