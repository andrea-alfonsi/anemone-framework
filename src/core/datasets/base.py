from abc import ABC, abstractmethod
from core.datasets.dataset_signature import DatasetSignature
from core.datasets.dataset_metadata import DatasetMetadata
from typing import Any, Dict, Sequence, Union
from numpy import ndarray


class BaseDataset(ABC):
    """
    A base class for datasets that provides common functionality
    and serves as a foundation for derived classes.

    This class can be extended by other classes to inherit shared
    attributes and methods.
    """

    _id: str
    _signature: DatasetSignature

    def __init__(self, name: str, signature: DatasetSignature):
        super().__init__()
        self._name = name
        self._signature = signature

    @property
    def signature(self) -> DatasetSignature:
        """
        Return the signature of the dataset.
        The signature is intended as as datatype of each instance of the dataset.
        For more infos about signaures check `src/signatureflow` directory
        """
        return self._signature

    @property
    def name(self):
        """
        Each dataset should have a human-readable name.
        This should used as identifier in UI.
        """
        return self._name

    @property
    def metadata(self) -> DatasetMetadata:
        """
        Build the metadata for the dataset.
        """
        return DatasetMetadata(name=self._name)

    @abstractmethod
    def __getitem__(self, key: Any) -> Any:
        """
        This method is used only to make simpler to interact with the underlying dataset structure
        and to make the package compatible with other libraries, but this should never be used in anemones's code.
        If you need to get some data from a dataset use the `select` methods, which returns always a ndarray (aka numpy's array)
        """
        pass

    @abstractmethod
    def select(self, query: Dict[str, Union[str, Sequence[str]]]) -> ndarray:
        """
        Use a select object to retrieve data from a dataset. The object can have 3 keys: "select", "conditions" and "order".
        Each subclass must implement this methods in order to comunicate with the underling technology and respond with the right data.
        The result should be a ndarray, where the first number of shape is the number of instances, and the other are the shape of the dataset.
        """
        pass
