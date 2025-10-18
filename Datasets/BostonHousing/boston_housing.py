from compress_pickle import dump, load
import pyndb
from pathlib import Path

HOME = Path.home()
DATASET_PATH = HOME / ".datasets" / "boston_housing.pyndb.gz"

pyndb.save_pickle = lambda obj, fn, *args, **kwargs: dump(obj, fn)
pyndb.load_pickle = lambda fn, *args, **kwargs: load(fn)

if not DATASET_PATH.exists():
    raise FileNotFoundError(f"Dataset not found at: {DATASET_PATH}")

db = pyndb.PYNDatabase(str(DATASET_PATH), filetype='pickled')

def load_x(num=150):
    return db.get("train_X").val[:num]

def load_y(num=150):
    return db.get("train_Y").val[:num]
