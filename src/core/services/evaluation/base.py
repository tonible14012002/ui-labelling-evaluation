from abc import ABC, abstractmethod
from src.core import domain
from typing import *


class IScorer(ABC):

    @classmethod
    @abstractmethod
    def score(cls, ground_truth: List[domain.Annotation], predictions: List[domain.Annotation]) -> Tuple[List[domain.Score], Optional[Dict[str, domain.Score]]]:
        """
        Calculate the score for a given sample.

        :param sample: The sample to score.
        :return: The score as a float.
        """
        pass