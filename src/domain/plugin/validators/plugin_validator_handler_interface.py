from abc import ABC, abstractmethod

from src.domain.plugin.entities.plugin_entity import PluginEntity


class IPluginValidatorHandler(ABC):

    def __init__(self, next_validator = None):
        self.next_validator = next_validator

    def validate(self, plugin: PluginEntity):
        self._check(plugin)
        if self.next_validator:
            self.next_validator.validate(plugin)

    @abstractmethod
    def _check(self, plugin: PluginEntity):
        pass
