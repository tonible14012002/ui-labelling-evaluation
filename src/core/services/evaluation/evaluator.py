from typing import *
from src.core.domain import *
from .scorer import IScorer

class Evaluator:
    def __init__(self, scorers: List[Type[IScorer]]):
        self.scorers = scorers
        
    def evaluate(self, dataset: List[Sample]) -> List[EvaluationResult]:
        eval_result = []
        for sample in dataset:
            ground_truths = sample.ground_truths
            predictions = sample.predictions
            for scorer in self.scorers:
                scores, tag_scores = scorer.score(ground_truths, predictions)
                eval_result.append(EvaluationResult(sample=sample, scores=scores, additional_scores=tag_scores))
        return eval_result
    