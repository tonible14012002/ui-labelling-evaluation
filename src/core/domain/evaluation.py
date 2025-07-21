from typing import *
from pydantic import BaseModel


class BBox(BaseModel):
    x: int
    y: int
    width: int
    height: int

class Annotation(BaseModel):
    bbox: BBox
    label: str
    value: str # tag
    author: str
    score: float
    result: Optional[str] = None  # Optional field for result, if needed

class Image(BaseModel):
    name: str
    type: str
    url: str
    
class Sample(BaseModel):
    input: Image
    ground_truths: List[Annotation] = []
    predictions: List[Annotation] = []

class Score(BaseModel):
    value: float
    name: str

class EvaluationResult(BaseModel):
    sample: Sample
    scores: List[Score] = []
    additional_scores: Optional[Dict[str, List[Score]]] = None