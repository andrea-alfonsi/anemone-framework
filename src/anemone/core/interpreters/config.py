"""
All the signautres that are requried to define a interpeter
"""

from typing import Optional
from attrs import frozen, field
from anemone.signatureflow import Signature


@frozen
class ConfigSignature:
    """
    The signature of the configurations for the interpreter
    """

    config: Optional[Signature] = field(kw_only=True)
