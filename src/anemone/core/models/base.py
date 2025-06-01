from abc import ABC, abstractmethod
from pathlib import Path
from anemone.core.models.model_signature import ModelSignature
from anemone.core.models.model_metadata import ModelMetadata
from anemone.core.models.mixin.trainable import TrainableMixin


class BaseModel(ABC):
    """
    A base class for models that provides common functionality
    and serves as a foundation for derived classes.

    This class can be extended by other classes to inherit shared
    attributes and methods.
    """

    _id: str
    _signature: ModelSignature

    def __init__(self, name: str, signature: ModelSignature):
        super().__init__()
        self._name = name
        self._signature = signature

    @property
    def signature(self) -> ModelSignature:
        return self._signature

    @property
    def name(self):
        return self._name

    @property
    def is_trainable(self) -> bool:
        return isinstance(self, TrainableMixin)

    @property
    def metadata(self) -> ModelMetadata:
        return ModelMetadata(name=self._name, trainable=self.is_trainable)
