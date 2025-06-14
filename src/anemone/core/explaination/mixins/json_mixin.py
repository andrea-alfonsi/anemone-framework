import json
from typing import Any


class JSONMixin:
    """
    Mixin to convert an explaination into a json automatically
    """

    raw_data: Any

    def to_json(self):
        """
        Convert the explaination to json
        """
        return json.dumps(self.raw_data)
