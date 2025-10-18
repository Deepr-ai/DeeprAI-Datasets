from compress_pickle import dump, load
import pyndb
from pathlib import Path

HOME = Path.home()
DATASET_PATH = HOME / ".datasets" / "mnist.pyndb.gz"

pyndb.save_pickle = lambda obj, fn, *args, **kwargs: dump(obj, fn)
pyndb.load_pickle = lambda fn, *args, **kwargs: load(fn)

if not DATASET_PATH.exists():
    raise FileNotFoundError(f"Dataset not found at: {DATASET_PATH}\n"
                            f"Make sure you installed the datasets package correctly.")

db = pyndb.PYNDatabase(str(DATASET_PATH), filetype='pickled')

# --- Dataset access functions ---
def load_x(num=60000):
    return db.get("train_X").val[:num]

def load_y(num=60000):
    return db.get("train_Y").val[:num]

def load_y_numeric(num=60000):
    return db.get("train_Y(num)").val[:num]
