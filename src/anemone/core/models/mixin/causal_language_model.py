"""
A Causal Language Model is designed to predict the *next* token in a sequence, given all the preceding tokens.
It learns a probability distribution over the next word in a sequence based on the words that have already appeared.

See also Masked Language Models, for models that predict a masked token
"""

from abc import ABC, abstractmethod
from typing import Any
from numpy import ndarray

TokenList = ndarray


class CausalLanguageModelMixin(ABC):
    """
    Abstract base class for Causal Language Models (CLMs).

    This class provides a common interface for interacting with different
    causal language models, abstracting away the specifics of various
    frameworks
    """

    @abstractmethod
    def encode(self, text: str) -> TokenList:
        """
        Abstract method to tokenize input text into a sequence of token
        """

    @abstractmethod
    def decode(self, token: TokenList) -> str:
        """
        Abstract method to convert a sequence of tokens into readable text
        """

    @abstractmethod
    def generate_text(self, prompt: str, max_new_tokens: int = 50, **kwargs: Any) -> str:
        """
        Abstract method to generate text based on a given prompt
        """
