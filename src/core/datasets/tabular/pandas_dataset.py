from core.datasets.base import BaseDataset
from typing import Any
import pandas as pd

class PandasDataset( BaseDataset ):
  def __init__(self, name, signature, datasource: pd.DataFrame ):
    super().__init__( name, signature )
    self._datasource = datasource

  def __getitem__(self, key):
    self._datasource[key]

  def select(self, query):
    raise NotImplementedError( "Not implemented yet")
    return super().select(query)