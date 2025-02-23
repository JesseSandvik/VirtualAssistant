from abc import ABC, abstractmethod


class IPluginValidator(ABC):

    @abstractmethod
    def validate(self, plugin) -> None:
        pass
