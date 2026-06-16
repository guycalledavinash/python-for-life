# Python Plugin Framework for Data Workflows

A compact, testable plugin framework for text-oriented data workflows. It shows how to model reusable transformations with object-oriented Python, compose them into pipelines, and optionally wire the workflow to a REST API.

## What is included

- A typed `BasePlugin` abstraction for all transformations
- Built-in plugins for uppercasing, removing whitespace, and normalizing whitespace
- A registry that builds plugin pipelines from friendly names
- A command-line runner for local text processing or REST-backed workflows
- A small REST client with timeouts and response validation
- A pytest suite that covers plugins, pipeline composition, and CLI behavior

## Project layout

```text
python-rest-oop/
├── api_client.py                  # REST client for /data and /result
├── main.py                        # CLI and pipeline runner
├── plugin_base.py                 # Plugin interface and validation helper
├── plugin_registry.py             # Built-in plugin lookup and construction
├── plugins/                       # Built-in plugins
├── test_plugins.py                # Pytest test suite
├── requirements.txt               # Runtime and test dependencies
└── pyproject.toml                 # Tooling configuration
```

## Quick start

```bash
cd python-rest-oop
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Process local text without making network calls:

```bash
python main.py --text " hello    world " --plugin normalize-whitespace --plugin uppercase
# Processing complete: HELLO WORLD
```

Use the default pipeline (`remove-whitespace`, then `uppercase`):

```bash
python main.py --text " hello world "
# Processing complete: HELLOWORLD
```

List available plugins:

```bash
python main.py --list-plugins
```

Run the REST-backed demo by omitting `--text`:

```bash
python main.py --base-url https://mockapi.io/demo
```

The REST mode expects:

- `GET /data` to return JSON with a string `text` field
- `POST /result` to accept JSON shaped like `{"result": "..."}`

## Adding a plugin

1. Create a class that inherits from `BasePlugin`.
2. Give it a unique `name` and helpful `description`.
3. Validate input with `ensure_text` before transforming it.
4. Export it from `plugins/__init__.py`.
5. Add it to `_BUILT_IN_PLUGINS` in `plugin_registry.py`.
6. Cover it with tests.

Example:

```python
from plugin_base import BasePlugin, ensure_text


class ReversePlugin(BasePlugin):
    name = "reverse"
    description = "Reverse the input text."

    def run(self, data: str) -> str:
        return ensure_text(data)[::-1]
```

## Testing

```bash
pytest
```
