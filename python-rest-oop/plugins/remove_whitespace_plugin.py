from plugin_base import BasePlugin

class RemoveWhitespacePlugin(BasePlugin):
    """Removes whitespace from a string."""

    def run(self, data):
        if isinstance(data, str):
            return ''.join(data.split())
        raise ValueError("Input must be a string")
