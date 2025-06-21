import pytest
import torch
from anemone.core.models.torch_model import TorchModel, ModelSignature
from anemone.core.models.mixin.trainable import TrainableMixin
from anemone.signatureflow.datatypes.tensor import Tensor


@pytest.fixture
def simple_model():
    class SimpleModel(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.fc = torch.nn.Linear(2, 1)

        def forward(self, x):
            return self.fc(x)

    return SimpleModel()


@pytest.fixture
def simple_model_signature():
    return ModelSignature(input={"data": Tensor(shape=(2,))}, output={"output": Tensor(shape=(1,))})


def test_model_predict(simple_model):
    x = torch.tensor([[2.0, 1.0]])
    output = simple_model(x)
    assert output.shape == torch.Size([1, 1])


def test_torch_train_mixin(simple_model, simple_model_signature):
    wrapper = TorchModel("torch_test", simple_model, simple_model_signature)
    assert wrapper.is_trainable() is False

    trainable_wrapper = type("TrainableTorchModel", (TorchModel, TrainableMixin), {})(
        "torch_trainable", simple_model, simple_model_signature
    )
    assert trainable_wrapper.is_trainable
