from typing import Optional, Dict, Any
from numpy import ndarray
from anemone.core.models.base import BaseModel
from anemone.core.datasets.base import BaseDataset


SQLLikeSelectQuery = str


class Context:
    """
    Encapsulate all the context relative to the current runtime
    """

    _selection: Optional[SQLLikeSelectQuery]
    _raw: Optional[ndarray]
    _model: Optional[BaseModel]
    _dataset: Optional[BaseDataset]
    _config: Optional[Dict[str, Any]]

    def __init__(
        self,
        model: Optional[BaseModel],
        dataset: Optional[BaseDataset],
        selection: Optional[SQLLikeSelectQuery],
        raw: Optional[ndarray],
        config: Optional[Dict[str, Any]],
    ):
        self._selection = selection
        self._raw = raw
        self._model = model
        self._dataset = dataset
        self._config = config

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
    def selection(self) -> SQLLikeSelectQuery:
        if self._selection is None:
            raise ValueError("No selection  provided")
        return self._selection

    @property
    def raw(self) -> ndarray:
        if self._raw is None:
            raise ValueError("No raw provided")
        return self._raw

    @property
    def config(self) -> Dict[str, Any]:
        if self._config is None:
            return {}
        return self._config
