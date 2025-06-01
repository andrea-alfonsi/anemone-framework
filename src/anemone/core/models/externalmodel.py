from anemone.core.models.model_signature import ModelSignature
from anemone.core.models.base import BaseModel
from typing import TypedDict, Optional
import subprocess
from io import UnsupportedOperation


class ProcessModelAPI(TypedDict):
    fit: Optional[str]
    predict: Optional[str]


class ExternalModel(BaseModel):
    """
    Any model that is handled by an external process or server
    """

    api: ProcessModelAPI

    def __init__(self, id, api: ProcessModelAPI, signature: ModelSignature):
        super().__init__(id, signature)
        self.api = api

    def save(self, folder):
        raise UnsupportedOperation("Cannot save a model when using an external service")

    def load(self, folder):
        raise UnsupportedOperation("Cannot load a model when using an external service")
