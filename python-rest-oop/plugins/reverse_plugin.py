"""Plugin that reverses text."""

from plugin_base import BasePlugin, ensure_text


class ReversePlugin(BasePlugin):
    """Reverse text while preserving every character."""

    name = "reverse"
    description = "Reverse the input text."

    def run(self, data: str) -> str:
        """Return ``data`` in reverse character order."""
        return ensure_text(data)[::-1]
