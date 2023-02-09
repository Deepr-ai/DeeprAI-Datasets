import shutil
from os.path import exists, expanduser
from os import mkdir
files = ["Datasets/BostonHousing/boston_housing.pyndb.gz", "Datasets/FashionMNIST/fashion_mnist.pyndb.gz",
         "Datasets/Iris/iris.pyndb.gz", "Datasets/MNIST/mnist.pyndb.gz"]
HOME = expanduser("~")

if not exists(f'{HOME}/.datasets'):
    mkdir(f'{HOME}/.datasets')

for file in files:
    src_file = "/path/to/source/file"
    dst_file = "/path/to/destination/file"

    shutil.move(src_file, dst_file)
