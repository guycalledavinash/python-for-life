"""Built-in text transformation plugins."""

from plugins.normalize_whitespace_plugin import NormalizeWhitespacePlugin
from plugins.remove_whitespace_plugin import RemoveWhitespacePlugin
from plugins.uppercase_plugin import UppercasePlugin

__all__ = [
    "NormalizeWhitespacePlugin",
    "RemoveWhitespacePlugin",
    "UppercasePlugin",
]
