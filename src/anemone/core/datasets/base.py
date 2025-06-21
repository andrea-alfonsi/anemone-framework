"""
Define the ase properties of a dataset class
"""

from abc import ABC, abstractmethod
from typing import Any, Sequence
from numpy import ndarray
from anemone.core.datasets.dataset_signature import DatasetSignature


class BaseDataset(ABC):
    """
    A base class for datasets that provides common functionality
    and serves as a foundation for derived classes.

    This class can be extended by other classes to inherit shared
    attributes and methods.
    """

    _signature: DatasetSignature
    _metadata: Any

    def __init__(self, signature: DatasetSignature, metadata: Any = None):
        super().__init__()
        self._signature = signature
        self._metadata = metadata

    @property
    def signature(self) -> DatasetSignature:
        """
        Return the signature of the dataset.
        The signature is intended as as datatype of each instance of the dataset.
        For more infos about signaures check `src/signatureflow` directory
        """
        return self._signature

    @property
    def metadata(self) -> Any:
        """
        Build the metadata for the dataset.
        """
        return self.metadata

    def get_features_names(self) -> Sequence[str]:
        """
        Get the columns that represents the features of the dataset
        """
        return [*self.signature.features.keys()]

    def get_targets_names(self) -> Sequence[str]:
        """
        Returns the list of comuns treatedas targets
        """
        return [*self.signature.targets.keys()]

    @abstractmethod
    def __getitem__(self, key: Any) -> Any:
        """
        This method is used only to make simpler to interact with the underlying dataset structure
        and to make the package compatible with other libraries, but this should never be used in anemones's code.
        If you need to get some data from a dataset use the `select` methods,
        which returns always a ndarray (aka numpy's array)
        """

    @abstractmethod
    def select(self, query: str) -> ndarray:
        """
        Use a sql like string to extract data from the dataset as numpy arrays
        """
