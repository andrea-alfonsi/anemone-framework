from typing import Any, Dict, List
from attrs import frozen, field
from anemone.signatureflow.datatypes.base import BaseDataType


@frozen
class Label(BaseDataType):
    """
    Select only one of the values among the vocab options
    """

    default: Any = field(kw_only=True)
    vocab: List[str] = field(kw_only=True)

    def validate(self, value: Any):
        if value is not None:
            if value not in self.vocab:
                raise ValueError(f"The field must be one of `{self.vocab}`. Got `{str(value)}`")
        super().validate(value)

    def serialize(self) -> Dict[str, Any]:
        res = super().serialize()
        res.setdefault("vocab", self.vocab)
        return res
