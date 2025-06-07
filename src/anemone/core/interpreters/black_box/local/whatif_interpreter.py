"""
Whatif Interpreter.

Simply run the model agains the raw inputs and returns the result
"""

from anemone.core.interpreters.base import BaseInterpreter


class WhatifInterpreter(BaseInterpreter):
    """
    Whatif interpreter. It simply run the model with the raw data provided
    """

    def run(self, config, context):
        return {"prediction": context.model.predict(context.raw)}
