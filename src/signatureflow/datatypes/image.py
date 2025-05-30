from signatureflow.datatypes.tensor import Tensor
from attrs import frozen, field
from enum import Enum
from base64 import b64decode
from PIL import Image as PILImage
from io import BytesIO
import numpy as np


class ImageFormat(Enum):
    RGBA = "RGBA"
    RGB = "RGB"
    GREY = "GREY"


class Image(Tensor):
    default = field(default=[0], kw_only=True)
    shape = field(default=[1, 1, 4], kw_only=True)
    format = field(default=ImageFormat.RGBA, kw_only=True)

    def validate(self, value):
        if isinstance( value, str ):
            data = b""
            if value.startswith("data:image/"):
                value = value[11:]
                if value.startswith("png;base64,") or value.startswith("jpg;base64,"):
                    data = b64decode(value[11:])
            if data == b"":
                raise ValueError("Format not recognized or data is missing")
            image = PILImage.open(BytesIO(data))
            raw = np.array(image)
            if not raw.shape == self.shape:
                raise ValueError(f"Invalid image data. Expected data with shape `{self.shape}`, got `{raw.shape}`")
            super().validate( np.squeeze(raw) )