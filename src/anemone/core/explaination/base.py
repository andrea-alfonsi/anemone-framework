"""
Represents the result of an explaination method
"""

from typing import Any


class BaseExplaination:
    """
    Base class from wich all the explainations inherit
    """

    def __init__(self, data: Any, metadata: Any):
        self._data = data
        self._metadata = metadata

    @property
    def raw_data(self):
        """
        Returns the data of the explaination
        """
        return self._data

    @property
    def metadata(self):
        """
        Returns the metadata of the explaination
        """
        return self._metadata
