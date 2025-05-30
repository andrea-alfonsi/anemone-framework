import pytest
from signatureflow.datatypes.scalar import Scalar
from core.datasets.pandas_dataset import PandasDataset
from core.datasets.dataset_signature import DatasetSignature
from core.interpreters.base import BaseInterpreter
from core.interpreters.interpreter_signature import InterpreterSignature
from core.models.torch_model import TorchModel
from core.models.model_signature import ModelSignature
import pandas as pd
import numpy as np
import torch


class ModelInterpreter(BaseInterpreter):
    def __init__(self, name):
        super().__init__(name, InterpreterSignature(config={}, output={}))

    def run(self, config, models, datasets, selection):
        for i, m in enumerate(models):
            m._model(torch.tensor(1.0))  # type: ignore
        return {}


@pytest.fixture
def simple_dataset():
    size = np.random.rand(30)
    price = size * 3
    return PandasDataset(
        "my dataset",
        DatasetSignature(signature={"size": Scalar(), "price": Scalar()}),
        pd.DataFrame({"size": size, "price": price}),
    )


@pytest.fixture
def simple_model():
    class Model(torch.nn.Module):
        def __init__(self):
            super(Model, self).__init__()
            self.fc = torch.nn.Linear(1, 1)  # Simple linear transformation

        def forward(self, x):
            x = x.float().unsqueeze(0)  # Convert to tensor and adjust shape
            return self.fc(x)

    return TorchModel("MyModel", Model(), ModelSignature(input={"size": Scalar()}, output={"price": Scalar()}))


def test_interpreter(simple_dataset, simple_model):
    interpreter = ModelInterpreter("ModelInterpreter")
    interpreter.run({}, [simple_model], [simple_dataset], [])
