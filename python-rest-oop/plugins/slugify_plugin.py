"""Plugin that converts text into URL-friendly slugs."""

import re

from plugin_base import BasePlugin, ensure_text

_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


class SlugifyPlugin(BasePlugin):
    """Convert text to a lowercase, hyphen-separated slug."""

    name = "slugify"
    description = "Convert text to a lowercase URL-friendly slug."

    def run(self, data: str) -> str:
        """Return ``data`` as a lowercase slug with duplicate separators removed."""
        normalized = ensure_text(data).casefold()
        return _NON_ALNUM_RE.sub("-", normalized).strip("-")
