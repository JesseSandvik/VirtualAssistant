from abc import ABC, abstractmethod


class IPluginValidator(ABC):

    def __init__(self, next_validator = None):
        self.next_validator = next_validator

    def validate(self, plugin):
        self._check(plugin)
        if self.next_validator:
            self.next_validator.validate(plugin)

    @abstractmethod
    def _check(self, plugin):
        pass
