from anemone.signatureflow.datatypes.base import BaseDataType
from attrs import frozen, field


@frozen
class String(BaseDataType):

    default: str = field(default="", kw_only=True)

    def validate(self, value):
        if not isinstance(value, (str)):
            raise ValueError(f"The field must be a string. Got `{str(value)}`")
        return super().validate(value)
