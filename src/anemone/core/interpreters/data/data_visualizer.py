"""
Thisinterpreter accpets a dataset and plots all the values into a scatter plot
"""

import logging
import numpy as np
from anemone.core.interpreters.base import BaseInterpreter
from anemone.core.interpreters.config import ConfigSignature
from anemone.core.explaination.base import BaseExplaination
from anemone.signatureflow.datatypes.label import Label


class DataVisualizerResult(BaseExplaination):
    pass


class DataVisualizer(BaseInterpreter):
    """
    Interpreter that returns a scatterplot
    """

    def run(self):
        if "algorithm" not in self.context.config:
            logging.warning(
                "algorithm key is not provided, falling back to the default one. "
                "This behaviour is discouraged because default method can change in future"
            )
            self.context.config.setdefault("algorithm", "pca")
        data_to_plot = self.context.dataset.select(self.context.selection)
        data_to_plot = data_to_plot.reshape(data_to_plot.shape[0], -1)
        data_mean = np.mean(data_to_plot, axis=0)
        data_to_plot_centered = data_to_plot - data_mean
        cov_matrix = np.cov(data_to_plot_centered, rowvar=False)
        _, eigenvectors = np.linalg.eigh(cov_matrix)
        top_2_eigenvectors = eigenvectors[:, -2:]
        projected_data = np.dot(data_to_plot_centered, top_2_eigenvectors)

        return DataVisualizerResult(projected_data, metadata=None)

    @staticmethod
    def get_config_signature():
        return ConfigSignature(config={"algorithm": Label(default="pca", vocab=["pca"])})
