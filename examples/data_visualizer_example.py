import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from anemone.core.interpreters.data.data_visualizer import DataVisualizer
from anemone.core.interpreters.base import RunContext
from anemone.core.datasets.tabular.pandas_dataset import PandasDataset


dataset = PandasDataset("My Dataset", None, pd.DataFrame({"a": range(5), "b": range(5), "c": range(5)}))
data_visualizer = DataVisualizer("My visualizer")
result = data_visualizer.run({}, RunContext(model=None, dataset=dataset, selection={"select": "*"}, raw=np.array([])))[
    "points"
]
print(result.shape)
plt.scatter(result[:, 0], result[:, 1])
plt.show()
