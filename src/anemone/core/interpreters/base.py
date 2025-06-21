"""
This module defines the `BaseInterpreter` abstract class, which provides a common
interface for all interpreter implementations. An interpreter takes a set of models,
a dataset, and a selection of data points, and produces an output.
"""

from abc import ABC, abstractmethod
from anemone.core.interpreters.config import ConfigSignature
from anemone.core.interpreters.context import Context
from anemone.core.explaination.base import BaseExplaination


class BaseInterpreter(ABC):
    """
    Abstract base class for interpreters, enforcing a `run` method
    """

    def __init__(self, context: Context):
        self._context = context

    @property
    def context(self) -> Context:
        """
        Get the context of the model
        """
        return self._context

    @abstractmethod
    def run(self) -> BaseExplaination:
        """
        Abstract method to execute the interpreter using the provided models, dataset,
        and selection criteria.
        """

    @staticmethod
    @abstractmethod
    def get_config_signature() -> ConfigSignature:
        """
        Returns the signaure for the config of the interpreter.
        """
