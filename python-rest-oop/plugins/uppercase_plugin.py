from plugin_base import BasePlugin

class UppercasePlugin(BasePlugin):
    """Converts text to uppercase."""

    def run(self, data):
        if isinstance(data, str):
            return data.upper()
        raise ValueError("Input must be a string")
