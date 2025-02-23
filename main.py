from src.domain import PluginRegistry
from src.application import PluginManager
from src.infrastructure import PluginLoader


if __name__ == "__main__":
    PluginLoader(PluginManager(PluginRegistry())).load_plugins()
