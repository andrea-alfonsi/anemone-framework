from anemone.core.models.model_signature import ModelSignature
from anemone.core.models.base import BaseModel
import torch


class TorchModel(BaseModel):
    _model: torch.nn.Module

    # Signaure must be provided because pytorch modulesare really flexible, and it can be impossible to understand the input or output when the first layer is a convolution
    def __init__(self, id, model: torch.nn.Module, signature: ModelSignature):
        super().__init__(id, signature)
        self._model = model

    def fit(self, X, y, **options):
        raise NotImplementedError("This method has not been implemented yet")
