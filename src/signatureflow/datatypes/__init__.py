from typing import Union
from .scalar import Scalar
from .string import String
from .tensor import Tensor
from .base import BaseDataType

DataType = Union[Scalar, String, Tensor]
