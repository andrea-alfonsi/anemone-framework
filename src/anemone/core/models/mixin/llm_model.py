"""
Define all the common methods for a model to be considered a llm
"""

from abc import ABC, abstractmethod
from typing import Sequence, Optional
from functools import lru_cache
import numpy as np


Tokens = np.ndarray


class LLMModelMixin(ABC):
    """
    Idicates that a model a LLM
    """

    def cache_generate(self, prompt: str):
        """
        Run the genetate method with cache for better performance and reduced cost when possible
        """
        if self._cached_generate_function is None:
            self._cached_generate_function = lru_cache()(self.generate)
        return self._cached_generate_function(prompt)

    def generate(self, prompt: str, output_number: int = 1) -> Sequence[str]:
        """
        takes a prompt and produces one or more responses
        """
        outputs = []
        for _ in range(output_number):
            outputs.append(self.decode(self.generate_with_mask(self.encode(prompt), None)))
        return outputs

    @abstractmethod
    def generate_with_mask(self, tokens: Tokens, mask: Optional[Tokens] = None) -> Tokens:
        """
        Run the llm model to enerate an answer but with the ability to mask tokens
        """

    @abstractmethod
    def encode(self, prompt: str) -> np.ndarray:
        """
        returns a list of tokens for a given text
        """

    @abstractmethod
    def decode(self, tokens: Tokens) -> str:
        """
        Convert the output back to a string
        """
