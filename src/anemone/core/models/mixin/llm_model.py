from abc import ABC, abstractmethod
from typing import Sequence

Token = int
Score = float


class LLMModelMixin(ABC):
    """
    Idicates that a model a LLM
    """

    @abstractmethod
    def generate(self, prompt: str) -> Sequence[str]:
        """
        takes a prompt and produces one or more responses
        """

    @abstractmethod
    def tokenize(self, prompt: str) -> Sequence[Token]:
        """
        returns a list of tokens for a given text
        """

    @abstractmethod
    def salience(self, prompt: str, output: Sequence[int], mask: Sequence[bool]) -> Sequence[Score]:
        """
        takes a prompt, a target output sequence, and a target mask specifying which output token(s) to explain,
        and returns scores for the preceding tokens
        """
