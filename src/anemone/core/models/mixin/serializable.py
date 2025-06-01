"""
This module defines the `SerializableMixin` class, which provides a generic interface
for saving and loading objects to and from a file path.
"""

from pathlib import Path


class SerializableMixin:
    """
    A mixin class that provides basic serialization methods for saving and loading objects.
    """

    def save(self, path: Path):
        """
        Saves the object to the specified file path. Should be implemented in subclasses.
        """
        raise NotImplementedError("Method `save` should be implemented in each child class")

    def load(self, path: Path):
        """
        Loads an object from the specified file path. Should be implemented in subclasses.
        """
        raise NotImplementedError("Method `load` should be implemented in each child class")
