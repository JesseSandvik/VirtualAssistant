from typing import List


class PluginRegistry(type):
    plugin_registries: List[type] = list()

    def __init__(cls, name, bases, attrs):
        super().__init__(cls)

        if name != 'PluginCore':
            PluginRegistry.plugin_registries.append(cls)
