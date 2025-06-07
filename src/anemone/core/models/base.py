"""
This module defines the `BaseModel` class, which serves as an abstract foundation for
machine learning models. It provides core attributes and methods to ensure consistency
and extensibility across derived models.
"""

from abc import ABC, abstractmethod
from numpy import ndarray
from anemone.core.models.model_signature import ModelSignature
from anemone.core.models.model_metadata import ModelMetadata
from anemone.core.models.mixin.trainable import TrainableMixin


class BaseModel(ABC):
    """
    An abstract base class for machine learning models, providing common functionality
    and ensuring consistent structure across implementations.
    """

    _id: str
    _signature: ModelSignature

    def __init__(self, name: str, signature: ModelSignature):
        super().__init__()
        self._name = name
        self._signature = signature

    @property
    def signature(self) -> ModelSignature:
        """
        Returns the model's input-output signature.
        """
        return self._signature

    @property
    def name(self):
        """
        Returns the model's name ( human-readable )
        """
        return self._name

    @property
    def is_trainable(self) -> bool:
        """
        Indicates whether the model supports training
        """
        return isinstance(self, TrainableMixin)

    @property
    def metadata(self) -> ModelMetadata:
        """
        Returns model metadata
        """
        return ModelMetadata(name=self._name, trainable=self.is_trainable)

    @abstractmethod
    def predict(self, inputs: ndarray) -> ndarray:
        """
        Simply run the model without other requirements.
        It should return a numpy array that complies with the model's output signature
        """
