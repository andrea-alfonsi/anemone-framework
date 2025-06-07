"""
This file provides an example on how to use the what-if interpreter
"""

import torch
from torch import nn
import pandas as pd
import numpy as np
from anemone.core.interpreters.black_box.local.whatif_interpreter import WhatifInterpreter
from anemone.core.interpreters.base import RunContext
from anemone.core.interpreters.interpreter_signature import InterpreterSignature
from anemone.core.models.torch_model import TorchModel
from anemone.core.models.model_signature import ModelSignature
from anemone.core.datasets.tabular.pandas_dataset import PandasDataset
from anemone.core.datasets.dataset_signature import DatasetSignature
from anemone.signatureflow.datatypes import Scalar


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


dataset = PandasDataset("My dataset", DatasetSignature(signature={}), pd.DataFrame({}))
model = TorchModel("My model", SimpleModel(1), ModelSignature(output={"value": Scalar()}, input={"value": Scalar()}))
interpreter = WhatifInterpreter("whatif interpreter", InterpreterSignature(config={}, output={}))
prediction = interpreter.run(RunContext(model=model, config={}, dataset=dataset), "", np.array([1]))

print(prediction)
