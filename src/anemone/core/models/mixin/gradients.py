"""
A framework-agnostic mixin class for adding gradient explainability features to
a deep learning model.
"""

from abc import ABC, abstractmethod
from typing import Optional, Tuple
from numpy import ndarray


PredictionAndGradientsType = Tuple[ndarray, ndarray]


class GradientsMixin(ABC):
    """
    Mixin that allows getting the computed gradients with respect to input.
    Useful for many explaiantion thechniques.
    """

    def compute_gradients(self, inputs: ndarray, target_index: Optional[int] = None, **kwargs) -> ndarray:
        """
        Compute the gradients with respect to input and returns their value. The prediction value is ignored
        """
        [_, grads] = self.predict_with_gradients(inputs, target_index, **kwargs)
        return grads

    @abstractmethod
    def predict_with_gradients(
        self, inputs: ndarray, target_index: Optional[int] = None, **kwargs
    ) -> PredictionAndGradientsType:
        """
        Computes the gradients of a specific model output with respect to the input.
        """
