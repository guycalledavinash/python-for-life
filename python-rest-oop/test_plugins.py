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
