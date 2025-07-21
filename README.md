## UI Labeling Evaluation

## Prerequisites
- Poetry
- Python >= 3.10

## Installation
```bash
git clone git@github.com:tonible14012002/ui-labelling-evaluation.git
cd ui-labelling-evaluation
poetry intsall
```

## Usage
```bash
poetry run python main.py --input <dataset dir> --output <result file dir>
```
Or use with pyenv
``` bash
pyenv virtualenv <env_name>
pyenv activate <env_name>
poetry install
python main.py --input <dataset dir> --output <result file dir>
```

## Dataset Format
```
dataset/
├── ground_truth/
│   ├── image1.json
│   ├── image2.json
│   └── ...
└── prediction/
    ├── image1.json
    ├── image2.json
    └── ...
```

**JSON structure**
```json
{
  "image": {
    "name": "Screenshot_2025-07-19_000.png",
    "path": "images/Screenshot_2025-07-19_000.png",
  },
  "annotations": [
    {
      "label": "Checkbox",
      "value": "checkbox",
      "bbox": {
        "x": 83,
        "y": 164,
        "width": 445,
        "height": 123
      },
      "author": "manual", // "llm"
      "score": 0.93
    }
  ]
}
```
The prediction replace  "manual" with "llm"
## 