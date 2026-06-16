"""Core plugin abstractions and helpers."""

from abc import ABC, abstractmethod


class BasePlugin(ABC):
    """Abstract base class for all text transformation plugins."""

    name: str = "base"
    description: str = "Base plugin interface"

    @abstractmethod
    def run(self, data: str) -> str:
        """Process text and return the transformed result."""


def ensure_text(data: str) -> str:
    """Validate that plugin input is text.

    Raises:
        ValueError: If ``data`` is not a string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string")
    return data
