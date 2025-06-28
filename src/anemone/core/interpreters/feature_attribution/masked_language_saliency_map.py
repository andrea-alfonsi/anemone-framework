from anemone.core.interpreters.base import BaseInterpreter
from anemone.core.explaination.base import BaseExplaination
from anemone.core.models.mixin.masked_language_model import MaskedLanguageModelMixin


class MaskedLanguageSaliecyMapExplaination(BaseExplaination):
    """
    pass
    """


class MaskedLanguageSaliencyMap(BaseInterpreter):
    """
    Get the most menaing words from the input of a masked language model.
    """

    @staticmethod
    def default_difference_measure(str1: str, str2: str) -> float:
        """
        Example function to calculate difference between2 srings
        """
        return len(str1) / len(str2) * 0.5

    @staticmethod
    def find_min_and_max(result: dict):
        _max = float("-inf")
        _min = float("inf")
        for val in result.values():
            _max = val if val > _max else _max
            _min = val if val < _min else _min
        return (_min, _max)

    def run(self):
        """
        Evaluate the saliency for each token
        """
        assert isinstance(
            self.context.model, MaskedLanguageModelMixin
        ), "The model must implement the MaskedLanguageModel mixin"
        message_to_explain = str(self.context.raw)
        mask = self.context.model.mask
        model = self.context.model
        baseline = model.fill_masks(message_to_explain, top_k=1)[0]["text"]
        words = list(baseline.split(" "))
        result = {}
        for i, word in enumerate(words):
            message = " ".join([w if n == i else mask for n, w in enumerate(words)])
            prediction = model.fill_masks(message, top_k=1)[0]["text"]
            result[(i, word)] = MaskedLanguageSaliencyMap.default_difference_measure(baseline, prediction)
        [_min, _max] = MaskedLanguageSaliencyMap.find_min_and_max(result)
        result = {k: (v - _min) / (_max - _min) for k, v in result}
        return MaskedLanguageSaliecyMapExplaination(result, {})
