from abc import ABC, abstractmethod


class PluginLoader(ABC):

    @abstractmethod
    def load_plugins(self):
        pass
