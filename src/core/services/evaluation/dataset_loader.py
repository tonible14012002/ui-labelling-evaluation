import json
from pathlib import Path
from src.core.domain import *

def load_dataset(dataset_dir: str) -> list[Sample]:
    dataset_dir = Path(dataset_dir)
    gt_dir = dataset_dir / "ground_truth"
    pred_dir = dataset_dir / "prediction"

    samples = []

    for gt_file in gt_dir.glob("*.json"):
        file_name = gt_file.name
        pred_file = pred_dir / file_name

        if not pred_file.exists():
            print(f"Warning: Prediction file not found for {file_name}")
            continue

        # Load ground truth
        with open(gt_file, "r") as f:
            gt_data = json.load(f)
            gt_annotations = [
                Annotation(
                    bbox=BBox(**ann["bbox"]),
                    label=ann["label"],
                    value=ann.get("value", ""),
                    author=ann.get("author", "manual"),
                    score=ann.get("score", 1.0),
                ) for ann in gt_data.get("annotations", [])
            ]

        # Load prediction
        with open(pred_file, "r") as f:
            pred_data = json.load(f)
            pred_annotations = [
                Annotation(
                    bbox=BBox(**ann["bbox"]),
                    label=ann["label"],
                    value=ann.get("value", ""),
                    author=ann.get("author", "llm"),
                    score=ann.get("score", 1.0),
                ) for ann in pred_data.get("annotations", [])
            ]

        image_info = gt_data.get("image", {})  # Assuming metadata about image exists in ground truth
        samples.append(
            Sample(
                input=Image(
                    name=image_info.get("name", file_name),
                    type=image_info.get("type", ""),
                    url=image_info.get("url", ""),
                    width=image_info.get("width", 0),
                    height=image_info.get("height", 0),
                ),
                ground_truths=gt_annotations,
                predictions=pred_annotations,
            )
        )
    return samples
 