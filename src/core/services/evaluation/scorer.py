from .base import IScorer
from typing import *
from src.core import domain
from collections import defaultdict

class IOUScorer(IScorer):
    
    @classmethod
    def score(cls, ground_truth: List[domain.Annotation], predictions: List[domain.Annotation], iou_threshold=0.5):

        matched = set()
        tp = 0
        
        #  For global metrics
        tag_counts = defaultdict(lambda: {"tp": 0, "pred": 0, "gt": 0})
        for gt in ground_truth:
            tag_counts[gt.value]["gt"] += 1
        
        for p in predictions:
            tag_counts[p.value]["pred"] += 1

        #  For per-tag metrics
        for p in predictions:
            best_iou = 0.0
            best_match = None

            for i, gt in enumerate(ground_truth):
                if gt.value != p.value or i in matched:
                    continue
                iou_score = iou(p.bbox, gt.bbox)
                if iou_score > best_iou:
                    best_iou = iou_score
                    best_match = i
                
            if best_match is not None and best_iou >= iou_threshold:
                matched.add(best_match)
                tp += 1
                tag_counts[p.value]["tp"] += 1

        fn = len(ground_truth) - tp
        fp = len(predictions) - tp
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0

        tag_counts = {
            tag: [
                domain.Score(value=tag_counts[tag]["gt"], name="False Negatives"),
                domain.Score(value=tag_counts[tag]["pred"], name="Predictions"),
                domain.Score(value=tag_counts[tag]["tp"], name="True Positives"),
            ]
            for tag in tag_counts
        }

        return [
            domain.Score(value=precision, name="Precision"),
            domain.Score(value=recall, name="Recall"),
            domain.Score(value=tp, name="True Positives"),
            domain.Score(value=fp, name="False Positives"),
            domain.Score(value=fn, name="False Negatives"),
        ], tag_counts
        

def iou(bbox1: domain.BBox, bbox2: domain.BBox) -> float:
    x1, y1 = bbox1.x, bbox1.y
    x2, y2 = x1 + bbox1.width, y1 + bbox1.height
    x3, y3 = bbox2.x, bbox2.y
    x4, y4 = x3 + bbox2.width, y3 + bbox2.height

    xi1, yi1 = max(x1, x3), max(y1, y3)
    xi2, yi2 = min(x2, x4), min(y2, y4)
    inter_w, inter_h = max(0, xi2 - xi1), max(0, yi2 - yi1)
    inter_area = inter_w * inter_h

    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x4 - x3) * (y4 - y3)
    union_area = box1_area + box2_area - inter_area

    return inter_area / union_area if union_area else 0