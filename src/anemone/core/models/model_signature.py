"""
This module defines the `ModelSignature` class, which represents the input-output
signature for machine learning models.
"""

from attrs import frozen, field
from anemone.signatureflow import Signature


@frozen
class ModelSignature:
    """
    Represents the input-output signature of a machine learning model.
    """

    input: Signature = field(kw_only=True)
    output: Signature = field(kw_only=True)
