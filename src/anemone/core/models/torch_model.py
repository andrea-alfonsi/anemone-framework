"""
This module defines a wrapper for PyTorch models, integrating them into the broader
model infrastructure.
"""

import torch
from numpy import ndarray
from anemone.core.models.model_signature import ModelSignature
from anemone.core.models.base import BaseModel


class TorchModel(BaseModel):
    """
    A wrapper for PyTorch models, integrating them with the base model infrastructure.

    This class encapsulates a PyTorch neural network model and provides a structured
    interface for managing model signatures. Given the flexibility of PyTorch modules,
    a signature must be provided to ensure correct input-output interpretation, especially
    when the first layer is a convolution.
    """

    _model: torch.nn.Module

    def __init__(self, name: str, model: torch.nn.Module, signature: ModelSignature):
        super().__init__(name, signature)
        self._model = model

    def fit(self, x: ndarray, y: ndarray, **options):
        """
        Train the model
        """
        raise NotImplementedError("This method has not been implemented yet")

    def predict(self, inputs):
        input_tensor = torch.tensor(inputs)
        return self._model(input_tensor)
