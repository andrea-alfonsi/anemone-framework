"""
This file provides an example on how to use the what-if interpreter
"""

import torch
from torch import nn
import pandas as pd
import numpy as np
from anemone.core.interpreters.black_box.local.whatif_interpreter import WhatifInterpreter
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
        x = torch.tensor(x, dtype=torch.float32)
        x = torch.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x


dataset = PandasDataset("My dataset", DatasetSignature(targets={}, features={}), pd.DataFrame({}))
model = TorchModel("My model", SimpleModel(1), ModelSignature(output={"value": Scalar()}, input={"value": Scalar()}))
context = Context(dataset=dataset, model=model, config=None, selection=None, raw=np.array([1]))
interpreter = WhatifInterpreter(context)
prediction = interpreter.run()

print(prediction)
