from typing import Dict, Optional, Union, Sequence
from numpy import ndarray
from anemone.core.models.base import BaseModel
from anemone.core.datasets.base import BaseDataset


class RunContext:
    """
    Encapsulate all the context relative to the current runtime
    """

    _selection: Optional[Dict[str, Union[str, Sequence[str]]]]
    _raw: Optional[ndarray]
    _model: Optional[BaseModel]
    _dataset: Optional[BaseDataset]

    def __init__(
        self,
        model: Optional[BaseModel],
        dataset: Optional[BaseDataset],
        selection: Optional[Dict[str, Union[str, Sequence[str]]]],
        raw: Optional[ndarray],
    ):
        self._selection = selection
        self._raw = raw
        self._model = model
        self._dataset = dataset

    @property
    def model(self) -> BaseModel:
        if self._model is None:
            raise ValueError("No model provided in the context")
        return self._model

    @property
    def dataset(self) -> BaseDataset:
        if self._dataset is None:
            raise ValueError("No dataset provided")
        return self._dataset

    @property
    def selection(self) -> Dict[str, Union[str, Sequence[str]]]:
        if self._selection is None:
            raise ValueError("No selection  provided")
        return self._selection

    @property
    def raw(self) -> ndarray:
        if self._raw is None:
            raise ValueError("No raw provided")
        return self._raw
