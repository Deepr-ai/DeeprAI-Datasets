from compress_pickle import dump, load
import pyndb
from os.path import expanduser
HOME = expanduser("~")

pyndb.save_pickle = lambda obj, fn, *args: dump(obj, fn)  # pyndb will try to send HIGHEST_PROTOCOL
pyndb.load_pickle = lambda fn, *args: load(fn)
db = pyndb.PYNDatabase(f"{HOME}/.datasets/mnist.pyndb.gz", filetype='pickled')
def load_x(num=60000):
    return db.get("train_X").val[:num]


def load_y(num=60000):
    return db.get("train_Y").val[:num]


def load_y_numeric(num=60000):
    return db.get("train_Y(num)").val[:num]
