from abc import ABC, abstractmethod


class IPluginLoader(ABC):

    @abstractmethod
    def load_plugins(self):
        pass
