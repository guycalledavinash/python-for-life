"""Plugin that converts text to uppercase."""

from plugin_base import BasePlugin, ensure_text


class UppercasePlugin(BasePlugin):
    """Convert text to uppercase."""

    name = "uppercase"
    description = "Convert all characters to uppercase."

    def run(self, data: str) -> str:
        """Return ``data`` converted to uppercase."""
        return ensure_text(data).upper()
