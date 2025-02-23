from src.domain import PluginRegistry, PluginValidator
from src.application import PluginManager
from src.infrastructure import FileSystemPluginLoader


if __name__ == "__main__":
    plugin_registry = PluginRegistry()
    plugin_loader = FileSystemPluginLoader()
    PluginManager(
        loader=plugin_loader,
        registry=plugin_registry,
        validator=PluginValidator
    ).load_plugins().register_plugins()

    print(plugin_registry.plugins)
