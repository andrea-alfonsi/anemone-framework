"""
Sequence Salience interpreter for blackbox LLMs
"""

import numpy as np
from anemone.core.interpreters.base import BaseInterpreter
from anemone.core.explaination.base import BaseExplaination
from anemone.core.models.mixin.llm_model import LLMModelMixin


class LLMSequenceSalienceExplaination(BaseExplaination):
    """
    The exlination based on the tokes score
    """


class LLMSequenceSalience(BaseInterpreter):
    """
    Interpreter that runs the llm model and returns a tuple containing
    the score associated to each token and the decoded token
    """

    def run(self):
        """
        Runthe given llm model and return the sequence salience map
        """

        if not isinstance(self.context.model, LLMModelMixin):
            raise ValueError("The model is not compatible with the interpreter")

        prompts = self.context.dataset.select(self.context.selection)
        saliency_scores = []

        for prompt in prompts:
            tokens = self.context.model.encode(prompt)
            generated = self.context.model.generate_with_mask(tokens, None)
            batch_saliency_scores = []
            for i in range(tokens.shape[1]):
                masked_tokens = np.ones_like(tokens)
                masked_tokens[0][i] = 0
                output = self.context.model.generate_with_mask(tokens, masked_tokens)
                if generated.shape[1] < output.shape[1]:
                    generated = np.pad(generated, ((0, 0), (0, output.shape[1] - generated.shape[1])), "constant")
                elif output.shape[1] < generated.shape[1]:
                    output = np.pad(output, ((0, 0), (0, generated.shape[1] - output.shape[1])), "constant")
                similarity = np.dot(generated, output) / (np.linalg.norm(generated) * np.linalg.norm(output))
                score = 1 - similarity
                batch_saliency_scores.append((score, self.context.model.decode(np.array(tokens[0][i]))))
            saliency_scores.append(batch_saliency_scores)

        return LLMSequenceSalienceExplaination(data=saliency_scores, metadata={})
