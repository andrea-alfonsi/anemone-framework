from abc import ABC, abstractmethod
from core.datasets.dataset_signature import DatasetSignature
from core.datasets.dataset_metadata import DatasetMetadata
from typing import Any


class BaseDataset(ABC):
    """
    A base class for datasets that provides common functionality
    and serves as a foundation for derived classes.

    This class can be extended by other classes to inherit shared
    attributes and methods.
    """

    _id: str
    _signature: DatasetSignature

    def __init__(self, id: str, signature: DatasetSignature):
        super().__init__()
        self._id = id
        self._signature = signature

    @property
    def signature(self) -> DatasetSignature:
        return self._signature

    @property
    def id(self):
        return self._id

    @property
    def metadata(self) -> DatasetMetadata:
        return DatasetMetadata(id=self._id)

    @abstractmethod
    def __getitem__(self, key: Any):
        pass

    @abstractmethod
    def select(self, query: str) -> Any:
        pass
