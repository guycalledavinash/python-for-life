"""Run the example REST-backed plugin workflow."""

from collections.abc import Iterable

from plugin_base import BasePlugin
from plugins.remove_whitespace_plugin import RemoveWhitespacePlugin
from plugins.uppercase_plugin import UppercasePlugin


def process_data(data: str, plugins: Iterable[BasePlugin]) -> str:
    """Apply each plugin to ``data`` in the order provided."""
    processed_data = data
    for plugin in plugins:
        processed_data = plugin.run(processed_data)
    return processed_data


def main() -> None:
    """Fetch data, transform it with the configured plugins, and post the result."""
    from api_client import MockAPIClient

    client = MockAPIClient(base_url="https://mockapi.io/demo")
    raw_data = client.fetch_data()
    plugins = [RemoveWhitespacePlugin(), UppercasePlugin()]

    processed_data = process_data(raw_data, plugins)

    client.post_result(processed_data)
    print("Processing complete:", processed_data)


if __name__ == "__main__":
    main()
