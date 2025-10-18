from pathlib import Path

HOME = Path.home()
DATASET_DIR = HOME / ".datasets"

DATASET_DIR.mkdir(exist_ok=True)
