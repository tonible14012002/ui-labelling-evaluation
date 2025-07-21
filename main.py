
from src.core.services.evaluation.dataset_loader import load_dataset
from src.core.services import evaluation as eval_service
import argparse
import json

def main(dataset_dir: str = "./dataset", output_file: str = "evaluation_results.json"):
    # Example usage of the dataset loader
    samples = load_dataset(dataset_dir)
    results = eval_service.Evaluator(
        scorers=[eval_service.IOUScorer]
    ).evaluate(samples)

    aggergate_tag_results = {
        "button": {
            "gt": 0,
            "pred": 0,
            "tp": 0 
        },
        "dropdown": {
            "gt": 0,
            "pred": 0,
            "tp": 0 
        },
        "input": {
            "gt": 0,
            "pred": 0,
            "tp": 0 
        },
        "checkbox": {
            "gt": 0,
            "pred": 0,
            "tp": 0
        },
    }

    for result in results:
        tag_scores = result.additional_scores

        for tag, score in tag_scores.items():
            if tag in aggergate_tag_results:
                aggergate_tag_results[tag]["gt"] += score[0].value
                aggergate_tag_results[tag]["pred"] += score[1].value
                aggergate_tag_results[tag]["tp"] += score[2].value
    
        # Write individual sample results to a JSON file
    for tag, counts in aggergate_tag_results.items():
        tp = counts["tp"]
        gt = counts["gt"]
        pred = counts["pred"]

        precision = tp / pred if pred > 0 else 0
        recall = tp / gt if gt > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

        print(f"{tag} - Precision: {precision:.2f}, Recall: {recall:.2f}, F1 Score: {f1:.2f}")

    with open(output_file, "w") as f:
        final_json = []
        for result in results:
            scores = result.scores
            sample = result.sample
            final_json.append({
                "scores": [score.model_dump() for score in scores],
                "sample": sample.model_dump(),

            })
        f.write(json.dumps(final_json, indent=4))
    
    print(f"Detail evaluation results saved to {output_file}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate UI detection results using IOU scorer.")
    parser.add_argument("--input", required=True, help="Path to the input JSON file.")
    parser.add_argument("--output", required=True, help="Path to the output JSON file.")
    args = parser.parse_args()
    main(
        dataset_dir=args.input,
        output_file=args.output
    )