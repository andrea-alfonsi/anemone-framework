from abc import ABC, abstractmethod
from typing import Sequence, Any, Dict
from core.interpreters.interpreter_signature import InterpreterSignature
from core.models.base import BaseModel
from core.datasets.base import BaseDataset


class BaseInterpreter(ABC):
    _name: str
    _signature: InterpreterSignature

    def __init__(self, name: str, signature: InterpreterSignature):
        self._name = name
        self._signature = signature

    @property
    def config(self):
        return self._signature.config

    @abstractmethod
    def run(
        self,
        config: Dict[str, Any],
        models: Sequence[BaseModel],
        dataset: BaseDataset,
        selection: str,
    ) -> Dict[str, Any]:
        """
        Run the interpreter with the given models, datasets, and seleccted points.
        """
        pass
