from typing import Any
from abc import ABC, abstractmethod


class TrainableMixin(ABC):
    """
    A mixin class to indicate that an ML model is trainable.

    This mixin provides methods for fitting the model.
    """

    @abstractmethod
    def fit(self, X: Any, y: Any, **kwargs: Any):
        raise NotImplementedError("Subclasses must implement the fit method.")
