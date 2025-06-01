from attrs import frozen, field
from typing import Any, Dict, Optional, Any, Sequence
from abc import ABC, abstractmethod
from numpy import ndarray

@frozen
class BaseDataType(ABC):
    default: Any = field(kw_only=True)
    required: Optional[bool] = field(default=True, kw_only=True)
    align: Optional[str] = field(default=None, kw_only=True)
    align_type: type = field(default=object, kw_only=True)

    def validate(self, value: Any):
        if self.required and value is None:
            raise ValueError(f"The field is required but no value is provided")

    def validate_context(self, data: Dict[str, Any]):
        if self.align is not None:
            if data.get(self.align) and isinstance(data.get(self.align), (self.align_type)):
                raise ValueError(
                    f"Expected field `{self.align}` to be present and to be of type `{ self.align_type.__name__ }`. Got `{ type(data.get( self.align )).__name__ }`"
                )

    def serialize(self) -> Dict[str, Any]:
        return {"required": self.required, "align": self.align, "type": type(self).__name__, "default": self.default}