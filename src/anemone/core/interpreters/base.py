"""
This module defines the `BaseInterpreter` abstract class, which provides a common
interface for all interpreter implementations. An interpreter takes a set of models,
a dataset, and a selection of data points, and produces an output.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Optional
from numpy import ndarray
from anemone.core.interpreters.interpreter_signature import InterpreterSignature
from anemone.core.models.base import BaseModel
from anemone.core.datasets.base import BaseDataset


@dataclass
class RunContext:
    """
    Encapsulate all the context relative to the current runtime
    """

    config: Dict[str, Any]
    model: BaseModel
    dataset: BaseDataset


class BaseInterpreter(ABC):
    """
    Abstract base class for interpreters, enforcing a `run` method
    """

    _name: str
    _signature: InterpreterSignature

    def __init__(self, name: str, signature: InterpreterSignature):
        self._name = name
        self._signature = signature

    @property
    def config_signature(self):
        """
        Property method that returns the interpreter's configuration from its signature.
        """
        return self._signature.config

    @abstractmethod
    def run(self, context: RunContext, selection: str, raw: ndarray) -> Dict[str, Any]:
        """
        Abstract method to execute the interpreter using the provided models, dataset,
        and selection criteria.
        """
