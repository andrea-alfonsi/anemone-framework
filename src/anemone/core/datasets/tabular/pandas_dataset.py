import pandas as pd
from anemone.core.datasets.base import BaseDataset


class PandasDataset(BaseDataset):
    """
    Wrapper around pandas dataframe to make it compatible with the package
    """

    def __init__(self, name, signature, datasource: pd.DataFrame):
        super().__init__(name, signature)
        self._datasource = datasource

    def __getitem__(self, key):
        return self._datasource[key]

    def select(self, query):
        if query.get("select", "*") == "*":
            if query.get("where") is None:
                return self._datasource.to_numpy()
        raise NotImplementedError("The provided query is not supported yet")
