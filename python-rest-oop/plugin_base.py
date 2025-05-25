from abc import ABC, abstractmethod

class BasePlugin(ABC):
    """Abstract base class for all plugins."""

    @abstractmethod
    def run(self, data):
        """Process the data and return the result."""
        pass
