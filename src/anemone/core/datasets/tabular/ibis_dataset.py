from anemone.core.datasets.base import BaseDataset
from typing import Any
import ibis

class IbisLocalDataset( BaseDataset ):
  def __init__(self, name, signature, datasource: Any ):
    super().__init__( name, signature )
    self._datasource = ibis.memtable(datasource)

  def __getitem__(self, key):
    raise NotImplementedError( "Not implemented yet")
    return super().__getitem__(key)

  def select(self, query):
    raise NotImplementedError( "Not implemented yet")
    return super().select(query)

class IbisRemoteDataset( BaseDataset ):
  def __init__(self, name, signature, connection: str ):
    super().__init__(name, signature)
    self._connection = ibis.connect( connection )

  def __getitem__(self, key):
    raise NotImplementedError( "Not implemented yet")
    return super().__getitem__(key)

  def select(self, query):
    raise NotImplementedError( "Not implemented yet")
    return super().select(query)
