"""
This file provides an example on how to use the what-if interpreter
"""

import torch
from torch import nn
import pandas as pd
import numpy as np
from anemone.core.interpreters.black_box.local.conterfactual_generator import CounterfactualGenerator
from anemone.core.interpreters.context import Context
from anemone.core.models.torch_model import TorchModel
from anemone.core.models.model_signature import ModelSignature
from anemone.core.datasets.tabular.pandas_dataset import PandasDataset
from anemone.core.datasets.dataset_signature import DatasetSignature
from anemone.signatureflow.datatypes.scalar import Scalar


class SimpleModel(nn.Module):
    """
    Simple torch model used  for demostration purpose only
    """

    def __init__(self, input_size):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 16)
        self.fc2 = nn.Linear(16, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        """
        The default method usedby pytorch to run inference
        """
        if not isinstance(x, torch.Tensor):
            x = torch.tensor(x, dtype=torch.float32)
        x = x.to(torch.float32)
        x = torch.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x


N = 10
dataset = PandasDataset(
    "df",
    DatasetSignature(features={"x1": Scalar(), "x2": Scalar()}, targets={"y": Scalar()}),
    pd.DataFrame({"x1": np.linspace(-1, 1, N), "x2": np.linspace(-1, 1, N), "y": np.round(np.linspace(0, 1, N))}),
)
model = TorchModel("My model", SimpleModel(2), ModelSignature(output={"value": Scalar()}, input={"value": Scalar()}))
context = Context(model=model, dataset=dataset, config=None, selection="select * from df", raw=None)
interpreter = CounterfactualGenerator(context)
prediction = interpreter.run()

print(prediction)
