"""
Token saliency
"""

from typing import List
from attrs import frozen, field
from anemone.signatureflow.datatypes.base import BaseDataType


@frozen
class TokenSaliency(BaseDataType):
    """
    A list of floats where each where the i-th value is the score of the i-th token
    """

    align: str = field(default="tokens", kw_only=True)
    default: List[float] = field(default=[])
