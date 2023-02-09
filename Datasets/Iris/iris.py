from compress_pickle import dump, load
import pyndb
from os.path import expanduser
HOME = expanduser("~")

pyndb.save_pickle = lambda obj, fn, *args: dump(obj, fn)  # pyndb will try to send HIGHEST_PROTOCOL
pyndb.load_pickle = lambda fn, *args: load(fn)
db = pyndb.PYNDatabase(f"{HOME}/.datasets/iris.pyndb.gz", filetype='pickled')

def load_x(num=150):
    return db.get("train_X").val[:num]


def load_y(num=150):
    return db.get("train_Y").val[:num]


def load_y_labels(num=150):
    return db.get("train_Y_labels").val[:num]
