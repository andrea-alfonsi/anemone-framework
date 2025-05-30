from core.datasets.base import BaseDataset
import pandas as pd


class PandasDataset(BaseDataset):
    _dataframe: pd.DataFrame

    def __init__(self, id, signature, dataframe: pd.DataFrame):
        super().__init__(id, signature)
        self._dataframe = dataframe

    def __getitem__(self, key):
        return self._dataframe.__getitem__(key)

    def select(self, query):
        raise NotImplementedError("Not implemented yet")
