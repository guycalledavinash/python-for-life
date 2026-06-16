"""Plugin that removes all whitespace from text."""

from plugin_base import BasePlugin, ensure_text


class RemoveWhitespacePlugin(BasePlugin):
    """Remove all whitespace characters from text."""

    name = "remove-whitespace"
    description = "Remove spaces, tabs, newlines, and other whitespace."

    def run(self, data: str) -> str:
        """Return ``data`` with every whitespace character removed."""
        return "".join(ensure_text(data).split())
