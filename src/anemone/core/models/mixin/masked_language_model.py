"""
See also Causal Language Models
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any


class MaskedLanguageModelMixin(ABC):
    """
    This class provides a common interface for interacting with different
    masked language models, abstracting away the specifics of various
    frameworks
    """

    @property
    @abstractmethod
    def mask(self) -> str:
        """
        Get the string to represent a mask e.g. '[MASK]' or '<mask>'
        """

    @property
    @abstractmethod
    def mask_token(self) -> int:
        """
        The the token id associated with the mask
        """

    @abstractmethod
    def fill_masks(self, text_with_masks: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        The `text_with_masks` should contain a special mask token (e.g., `[MASK]`, `<mask>`)
        that the model will predict.

        Returns:
            `{'text': 'The capital of France is Paris.', 'score': 0.99, 'token_str': 'Paris', 'position': 5}`).
        """
