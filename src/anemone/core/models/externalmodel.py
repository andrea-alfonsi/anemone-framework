"""
This module defines the `ExternalModel` class, which represents models handled by
external processes or servers. It provides an interface for integrating externally
managed models into the broader system
"""

from typing import TypedDict, Optional
from anemone.core.models.model_signature import ModelSignature
from anemone.core.models.base import BaseModel


class ProcessModelAPI(TypedDict):
    """
    A model wrapper for externally managed models that interact via predefined API endpoints.
    """

    fit: Optional[str]
    predict: Optional[str]


class ExternalModel(BaseModel):
    """
    Any model that is handled by an external process or server
    """

    api: ProcessModelAPI

    def __init__(self, name, api: ProcessModelAPI, signature: ModelSignature):
        super().__init__(name, signature)
        self.api = api
