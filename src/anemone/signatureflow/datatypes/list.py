from typing import Any, Dict
from attrs import frozen, field
from anemone.signatureflow.datatypes.base import BaseDataType


@frozen
class List(BaseDataType):
    """
    Datatype for generic string
    """

    default: Any = field(default=[], kw_only=True)
    items_type: type = field(default=object, kw_only=True)

    def validate(self, value: Any):
        if value is not None:
            if not isinstance(value, list):
                raise ValueError(f"The field must be a list. Got `{str(value)}`")
            if not all(isinstance(item, self.items_type) for item in value):
                raise ValueError(f"The field must be a list of integers or floats. Got `{str(value)}`")
        super().validate(value)

    def serialize(self) -> Dict[str, Any]:
        res = super().serialize()
        res.setdefault("items_type", type(self.items_type).__name__)
        return res


@frozen
class StringList(List):
    """
    List of strings
    """

    items_type: type = field(default=str, kw_only=True)
