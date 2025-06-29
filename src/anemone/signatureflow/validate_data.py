from collections import defaultdict
from typing import Any, Dict, Sequence

from anemone.signatureflow.signature import Signature


def validate_data(signature: Signature, data: Dict[str, Any]) -> Dict[str, Sequence[str]]:
    """
    Check if the data is comaptible with the given signature.
    Retuns a dictionary of errors that try to explain why the values are not valid.
    """
    errors: defaultdict[str, list[str]] = defaultdict(list)
    for key, dtype in signature.items():
        try:
            dtype.validate(data.get(key))
            dtype.validate_context(data)
        except ValueError as e:
            errors[key].append(str(e))
    return dict(errors)
