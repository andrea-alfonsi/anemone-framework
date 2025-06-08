"""
Thisinterpreter accpets a dataset and plots all the values into a scatter plot
"""

import logging
import numpy as np
from anemone.core.interpreters.base import BaseInterpreter, InterpreterSignature
from anemone.signatureflow.datatypes.label import Label
from anemone.signatureflow.datatypes.tensor import Tensor


class DataVisualizer(BaseInterpreter):
    """
    Interpreter that returns a scatterplot
    """

    def __init__(self, name):
        super().__init__(
            name,
            InterpreterSignature(
                config={"dimensionalityReduction": Label(default="pca", vocab=["pca"])},
                output={"points": Tensor(shape=(-1, 2))},
            ),
        )

    def run(self, config, context):
        if "dimensionalityReduction" not in config:
            logging.warning(
                "dimensionalityReduction key is not provided, falling back to the default one. "
                "This behaviour is discouraged because default method can change in future"
            )
            config.setdefault("dimensionalityReduction", "pca")
        data_to_plot = context.dataset.select(context.selection)
        data_to_plot = data_to_plot.reshape(data_to_plot.shape[0], -1)
        data_mean = np.mean(data_to_plot, axis=0)
        data_to_plot_centered = data_to_plot - data_mean
        cov_matrix = np.cov(data_to_plot_centered, rowvar=False)
        _, eigenvectors = np.linalg.eigh(cov_matrix)
        top_2_eigenvectors = eigenvectors[:, -2:]
        projected_data = np.dot(data_to_plot_centered, top_2_eigenvectors)

        return {"points": projected_data}
