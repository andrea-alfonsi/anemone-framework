from abc import ABC, abstractmethod
from pathlib import Path
from core.models.model_signature import ModelSignature
from core.models.model_metadata import ModelMetadata
from core.models.mixin.trainable import TrainableMixin


class BaseModel(ABC):
    """
    A base class for models that provides common functionality
    and serves as a foundation for derived classes.

    This class can be extended by other classes to inherit shared
    attributes and methods.
    """

    _id: str
    _signature: ModelSignature

    def __init__(self, id: str, signature: ModelSignature):
        super().__init__()
        self._id = id
        self._signature = signature

    @property
    def signature(self) -> ModelSignature:
        return self._signature

    @property
    def id(self):
        return self._id

    @property
    def is_trainable(self) -> bool:
        return isinstance(self, TrainableMixin)

    @property
    def metadata(self) -> ModelMetadata:
        return ModelMetadata(id=self._id, trainable=self.is_trainable)
