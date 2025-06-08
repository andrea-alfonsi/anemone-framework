from abc import ABC
from typing import Any, Dict, Optional
from attrs import frozen, field


@frozen
class BaseDataType(ABC):
    """
    Base datatype from which all theothers must inherit
    """

    default: Any = field(kw_only=True)
    required: Optional[bool] = field(default=True, kw_only=True)
    align: Optional[str] = field(default=None, kw_only=True)
    align_type: type = field(default=object, kw_only=True)

    def validate(self, value: Any):
        """
        Check if the data received iscompatible with this datatype
        """
        if self.required and value is None:
            raise ValueError("The field is required but no value is provided")

    def validate_context(self, data: Dict[str, Any]):
        """
        Check if constraints to other fields are respected
        """
        if self.align is not None:
            if data.get(self.align) and isinstance(data.get(self.align), (self.align_type)):
                raise ValueError(
                    f"Expected field `{self.align}` to be present and to be of type `{self.align_type.__name__}`. "
                    f"Got `{type(data.get(self.align)).__name__}`"
                )

    def serialize(self) -> Dict[str, Any]:
        """
        Convert this datatype into a dict
        """
        return {"required": self.required, "align": self.align, "type": type(self).__name__, "default": self.default}
