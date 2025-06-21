import pandas as pd
import duckdb
from anemone.core.datasets.base import BaseDataset


class PandasDataset(BaseDataset):
    """
    Wrapper around pandas dataframe to make it compatible with the package
    """

    def __init__(self, name, signature, datasource: pd.DataFrame):
        super().__init__(signature)
        self._name = name
        self._datasource = datasource

    def __getitem__(self, key):
        return self._datasource[key]

    def select(self, query):
        return duckdb.query_df(self._datasource, self._name, query).df().to_numpy()
