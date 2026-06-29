"""Run text through a configurable plugin workflow."""

import argparse
from collections.abc import Iterable, Sequence

from plugin_base import BasePlugin
from plugin_registry import available_plugins, build_plugins

DEFAULT_PLUGINS = ("remove-whitespace", "uppercase")
DEFAULT_BASE_URL = "https://mockapi.io/demo"


def process_data(data: str, plugins: Iterable[BasePlugin]) -> str:
    """Apply each plugin to ``data`` in the order provided."""
    processed_data = data
    for plugin in plugins:
        processed_data = plugin.run(processed_data)
    return processed_data


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments for the workflow runner."""
    registry = available_plugins()
    parser = argparse.ArgumentParser(
        description="Run text through a configurable plugin pipeline.",
    )
    parser.add_argument(
        "--text",
        help="Text to process locally. If omitted, input is fetched from the REST API.",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=(
            "REST API base URL used when --text is omitted "
            f"(default: {DEFAULT_BASE_URL})."
        ),
    )
    parser.add_argument(
        "--plugin",
        action="append",
        choices=sorted(registry),
        dest="plugins",
        help=(
            "Plugin to apply, in order. Repeat this option to build a pipeline. "
            f"Defaults to: {', '.join(DEFAULT_PLUGINS)}."
        ),
    )
    parser.add_argument(
        "--list-plugins",
        action="store_true",
        help="List available plugins and exit.",
    )
    parser.add_argument(
        "--show-pipeline",
        action="store_true",
        help="Print the selected plugin pipeline before processing.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """Fetch or accept text, transform it, optionally post it, and print the result."""
    args = parse_args(argv)
    registry = available_plugins()

    if args.list_plugins:
        for name, plugin_class in sorted(registry.items()):
            print(f"{name}: {plugin_class.description}")
        return 0

    plugin_names = args.plugins or list(DEFAULT_PLUGINS)
    plugins = build_plugins(plugin_names)

    if args.show_pipeline:
        print("Pipeline:", " -> ".join(plugin.name for plugin in plugins))

    if args.text is None:
        from api_client import MockAPIClient

        client = MockAPIClient(base_url=args.base_url)
        raw_data = client.fetch_data()
        processed_data = process_data(raw_data, plugins)
        client.post_result(processed_data)
    else:
        processed_data = process_data(args.text, plugins)

    print("Processing complete:", processed_data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
