from anemone.signatureflow.datatypes.base import BaseDataType
from typing import Union, Optional
from attrs import frozen, field


@frozen
class Scalar(BaseDataType):
    Number = Union[int, float]

    default: Number = field(default=0.0, kw_only=True)
    min: Optional[Number] = field(default=None, kw_only=True)
    max: Optional[Number] = field(default=None, kw_only=True)
    step: Optional[Number] = field(default=None, kw_only=True)

    def validate(self, value):
        if value is not None:
            if not isinstance(value, (int, float)):
                raise ValueError(f"The field must be an integer or a float. Got `{str(value)}`")
        return super().validate(value)

    def serialize(self):
        partial = super().serialize()
        partial["min"] = self.min
        partial["max"] = self.max
        partial["step"] = self.step
        return partial
