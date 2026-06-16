"""Registry for looking up available plugins by name."""

from collections.abc import Iterable

from plugin_base import BasePlugin
from plugins import NormalizeWhitespacePlugin, RemoveWhitespacePlugin, UppercasePlugin

PluginType = type[BasePlugin]

_BUILT_IN_PLUGINS: tuple[PluginType, ...] = (
    NormalizeWhitespacePlugin,
    RemoveWhitespacePlugin,
    UppercasePlugin,
)


def available_plugins() -> dict[str, PluginType]:
    """Return built-in plugins keyed by their command-line names."""
    return {plugin.name: plugin for plugin in _BUILT_IN_PLUGINS}


def build_plugins(names: Iterable[str]) -> list[BasePlugin]:
    """Instantiate plugins from their registered names.

    Raises:
        ValueError: If any plugin name is unknown.
    """
    registry = available_plugins()
    plugins: list[BasePlugin] = []

    for name in names:
        try:
            plugin_class = registry[name]
        except KeyError as exc:
            options = ", ".join(sorted(registry))
            raise ValueError(f"Unknown plugin '{name}'. Available plugins: {options}") from exc
        plugins.append(plugin_class())

    return plugins
