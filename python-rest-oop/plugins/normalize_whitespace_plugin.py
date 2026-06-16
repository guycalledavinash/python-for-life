"""Plugin that collapses repeated whitespace into single spaces."""

from plugin_base import BasePlugin, ensure_text


class NormalizeWhitespacePlugin(BasePlugin):
    """Normalize whitespace without removing word boundaries."""

    name = "normalize-whitespace"
    description = "Collapse repeated whitespace and trim leading/trailing spaces."

    def run(self, data: str) -> str:
        """Return ``data`` with whitespace collapsed to single spaces."""
        return " ".join(ensure_text(data).split())
