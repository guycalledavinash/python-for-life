"""Tests for the example plugin workflow."""

import pytest

from main import main, process_data
from plugin_registry import available_plugins, build_plugins
from plugins.normalize_whitespace_plugin import NormalizeWhitespacePlugin
from plugins.remove_whitespace_plugin import RemoveWhitespacePlugin
from plugins.reverse_plugin import ReversePlugin
from plugins.slugify_plugin import SlugifyPlugin
from plugins.uppercase_plugin import UppercasePlugin


def test_uppercase_plugin() -> None:
    plugin = UppercasePlugin()
    assert plugin.run("hello") == "HELLO"


def test_remove_whitespace_plugin() -> None:
    plugin = RemoveWhitespacePlugin()
    assert plugin.run("a b\tc\n") == "abc"


def test_normalize_whitespace_plugin() -> None:
    plugin = NormalizeWhitespacePlugin()
    assert plugin.run("  hello\tbeautiful\nworld  ") == "hello beautiful world"


def test_reverse_plugin() -> None:
    plugin = ReversePlugin()
    assert plugin.run("desserts") == "stressed"


def test_slugify_plugin() -> None:
    plugin = SlugifyPlugin()
    assert plugin.run("  Python REST + OOP!  ") == "python-rest-oop"


def test_invalid_input() -> None:
    plugin = UppercasePlugin()
    with pytest.raises(ValueError, match="Input must be a string"):
        plugin.run(123)  # type: ignore[arg-type]


def test_process_data_applies_plugins_in_order() -> None:
    plugins = [NormalizeWhitespacePlugin(), UppercasePlugin()]
    assert process_data(" hello    world ", plugins) == "HELLO WORLD"


def test_build_plugins_from_registry() -> None:
    plugins = build_plugins(["normalize-whitespace", "uppercase"])
    assert [plugin.name for plugin in plugins] == ["normalize-whitespace", "uppercase"]


def test_build_plugins_rejects_unknown_name() -> None:
    with pytest.raises(ValueError, match="Unknown plugin 'missing'"):
        build_plugins(["missing"])


def test_available_plugins_includes_built_ins() -> None:
    assert set(available_plugins()) == {
        "normalize-whitespace",
        "remove-whitespace",
        "reverse",
        "slugify",
        "uppercase",
    }


def test_cli_processes_local_text(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main([
        "--text",
        " hello    world ",
        "--plugin",
        "normalize-whitespace",
        "--plugin",
        "uppercase",
    ])

    assert exit_code == 0
    assert capsys.readouterr().out == "Processing complete: HELLO WORLD\n"


def test_cli_lists_plugins(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["--list-plugins"])

    assert exit_code == 0
    output = capsys.readouterr().out
    assert "normalize-whitespace: Collapse repeated whitespace" in output
    assert "remove-whitespace: Remove spaces" in output
    assert "reverse: Reverse the input text" in output
    assert "slugify: Convert text to a lowercase URL-friendly slug" in output
    assert "uppercase: Convert all characters" in output


def test_cli_can_show_pipeline(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main([
        "--text",
        "Hello World",
        "--plugin",
        "slugify",
        "--show-pipeline",
    ])

    assert exit_code == 0
    assert capsys.readouterr().out == (
        "Pipeline: slugify\n"
        "Processing complete: hello-world\n"
    )


class FakeResponse:
    def __init__(self, payload: object, status_ok: bool = True) -> None:
        self.payload = payload
        self.status_ok = status_ok

    def raise_for_status(self) -> None:
        if not self.status_ok:
            raise RuntimeError("HTTP error")

    def json(self) -> object:
        return self.payload


class FakeSession:
    def __init__(self) -> None:
        self.posts: list[tuple[str, object, float]] = []

    def get(self, url: str, **kwargs: object) -> FakeResponse:
        assert url == "https://example.test/data"
        assert kwargs == {"timeout": 2.5}
        return FakeResponse({"text": "hello api"})

    def post(self, url: str, **kwargs: object) -> FakeResponse:
        self.posts.append((url, kwargs["json"], kwargs["timeout"]))
        return FakeResponse({"ok": True})


def test_api_client_uses_injected_session() -> None:
    from api_client import MockAPIClient

    session = FakeSession()
    client = MockAPIClient("https://example.test/", timeout=2.5, session=session)

    assert client.fetch_data() == "hello api"
    assert client.post_result("HELLO API") == {"ok": True}
    assert session.posts == [(
        "https://example.test/result",
        {"result": "HELLO API"},
        2.5,
    )]
