from typing import Union, Sequence
from attrs import frozen, field
from numpy import ndarray
from anemone.signatureflow.datatypes.base import BaseDataType


@frozen
class Tensor(BaseDataType):
    Number = Union[int, float]

    default: Sequence[Number] = field(default=[], kw_only=True)
    shape: Sequence[Union[int, None]]

    def validate(self, value):
        if value is not None:
            if not isinstance(value, ndarray):
                if not isinstance(value, list):
                    raise ValueError(f"The field must be a list or numpy array. Got `{str(value)}`")
                if not all(isinstance(item, (int, float)) for item in value):
                    raise ValueError(f"The field must be a list of integers or floats. Got `{str(value)}`")
        super().validate(value)
