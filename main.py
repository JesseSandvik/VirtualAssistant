from src.domain import PluginRegistry
from src.infrastructure import PluginLoader


if __name__ == "__main__":
    plugin_registry = PluginRegistry()
    plugin_loader = PluginLoader(plugin_registry)
    plugin_loader.discover_plugins()
