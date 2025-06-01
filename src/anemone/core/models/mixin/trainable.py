"""
This module defines the `TrainableMixin` class, which provides a standardized interface
for machine learning models that support training.
"""

from typing import Any
from abc import ABC, abstractmethod


class TrainableMixin(ABC):
    """
    A mixin class that marks a machine learning model as trainable, requiring implementation
    of the `fit` method.
    """

    @abstractmethod
    def fit(self, x: Any, y: Any, **kwargs: Any):
        """
        Abstract method for fitting the model. Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the fit method.")
