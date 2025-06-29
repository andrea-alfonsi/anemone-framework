"""
utilities to serialize a signature into various structures
"""

from typing import Any, Dict
from anemone.signatureflow.signature import Signature


def serialize(signature: Signature) -> Dict[str, Any]:
    """
    Convert a Signature into a dictionary
    """
    return {k: v.serialize() for k, v in signature.items()}
