"""
This files shows an exmpale of how to use the data visualizer interpreter
"""

import pandas as pd
from anemone.core.interpreters.data.data_visualizer import DataVisualizer
from anemone.core.interpreters.context import Context
from anemone.core.datasets.tabular.pandas_dataset import PandasDataset


dataset = PandasDataset("df", None, pd.DataFrame({"a": range(5), "b": range(5), "c": range(5)}))
context = Context(dataset=dataset, model=None, selection="select * from df", raw=None, config={"algorithm": "pca"})
data_visualizer = DataVisualizer(context)
result = data_visualizer.run()
