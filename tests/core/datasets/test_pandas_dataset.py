import pytest
from signatureflow.datatypes.scalar import Scalar
from signatureflow.datatypes.string import String
from core.datasets.pandas_dataset import PandasDataset
from core.datasets.dataset_signature import DatasetSignature
import pandas as pd


@pytest.fixture
def simple_dataframe():
    return pd.DataFrame({"name": ["A", "B", "C"], "age": [1, 2, 3]})


@pytest.fixture
def simple_dataset_signature():
    return DatasetSignature(signature={"name": String(), "age": Scalar()})


def test_simple_select(simple_dataframe, simple_dataset_signature):
    dataset = PandasDataset("my_dataset", simple_dataset_signature, simple_dataframe)
    assert list(dataset[["name"]].values.reshape(-1)) == ["A", "B", "C"]
