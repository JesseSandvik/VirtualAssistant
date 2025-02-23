from src.application import PluginManager
from src.infrastructure import FileSystemPluginLoader, FileSystemPluginRegistry, FileSystemPluginValidator


if __name__ == "__main__":
    plugin_registry = FileSystemPluginRegistry()
    plugin_loader = FileSystemPluginLoader()
    plugin_validator = FileSystemPluginValidator()
    PluginManager(
        loader=plugin_loader,
        registry=plugin_registry,
        validator=plugin_validator
    ).load_plugins().register_plugins()

    print(plugin_registry.registry)
