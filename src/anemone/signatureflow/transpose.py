"""
Utility to convert a signatureitno another
"""

from typing import Sequence, Tuple
from anemone.signatureflow.signature import Signature


def transpose(source: Signature, target: Signature) -> Sequence[Tuple[str, str]]:
    """
    Generate a map to convert from a signature into another
    """
    mapping = []
    source_keys = source.keys()
    target_keys = target.keys()
    remaining = []

    for key in target_keys:
        if key in source_keys:
            if not type(source[key]) == type(target[key]):
                raise ValueError("The 2 signatures are not compatible")
            else:
                source_keys = [k for k in source_keys if not k == key]
        else:
            remaining.append(key)
    for key in remaining:
        for skey in source_keys:
            if type(source[skey]) == type(target[key]):
                mapping.append((skey, key))
                break
        else:
            raise ValueError(f"No key found comaptible with {key}")
    return mapping
