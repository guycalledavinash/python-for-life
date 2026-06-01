import pytest
from plugins.uppercase_plugin import UppercasePlugin
from plugins.remove_whitespace_plugin import RemoveWhitespacePlugin


def test_uppercase_plugin():
    plugin = UppercasePlugin()
    assert plugin.run("hello") == "HELLO"


def test_remove_whitespace_plugin():
    plugin = RemoveWhitespacePlugin()
    assert plugin.run("a b c") == "abc"


def test_invalid_input():
    plugin = UppercasePlugin()
    with pytest.raises(ValueError):
        plugin.run(123)


def test_process_data_applies_plugins_in_order():
    from main import process_data

    plugins = [RemoveWhitespacePlugin(), UppercasePlugin()]
    assert process_data(" hello world ", plugins) == "HELLOWORLD"
