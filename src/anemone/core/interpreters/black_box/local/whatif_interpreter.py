"""
Whatif Interpreter.

Simply run the model agains the raw inputs and returns the result
"""

from anemone.core.interpreters.base import BaseInterpreter
from anemone.core.interpreters.config import ConfigSignature
from anemone.core.explaination.base import BaseExplaination


class WhatifExplainnation(BaseExplaination):
    """
    What if explaination result
    """

    def __init__(self, data):
        super().__init__(data, None)


class WhatifInterpreter(BaseInterpreter):
    """
    Whatif interpreter. It simply run the model with the raw data provided
    """

    def run(self):
        return WhatifExplainnation(self.context.model.predict(self.context.raw))

    @staticmethod
    def get_config_signature():
        return ConfigSignature(config=None)
