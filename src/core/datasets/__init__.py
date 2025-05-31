from core.datasets.base import BaseDataset
from signatureflow import transpose
import numpy as np

def append( dataset: BaseDataset, *datasets: BaseDataset, name = "AppendDataset" ) -> BaseDataset :
  class AppendDatasets( BaseDataset ):

    def __init__(self, name, signature, *datasets: BaseDataset):
      super().__init__(name, signature)
      self._datasets = datasets

    def __getitem__(self, key):
      for dataset in self._datasets:
        yield dataset.__getitem__( key )

    def select(self, query):
      result = self._datasets[0].select( query )
      for dataset in self._datasets[1:]:
        data = dataset.select( query )
        result = np.concat( (result, data), axis=0 )
      return result

  if len( datasets ) > 0:
    s = dataset.signature.signature
    for d in datasets:
      if not len(transpose( s, d.signature.signature )) == 0:
        raise ValueError(f"The datasets `{dataset.name}` and `{d.name}` are not compatible beccause they have different signatures")
    return AppendDatasets( name, dataset.signature, dataset, *datasets )
  else:
    return dataset