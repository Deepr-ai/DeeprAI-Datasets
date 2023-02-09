from setuptools import setup
from setuptools import find_packages
import shutil
from os.path import exists, expanduser
from os import mkdir
files = ["Datasets/BostonHousing/boston_housing.pyndb.gz", "Datasets/FashionMNIST/fashion_mnist.pyndb.gz",
         "Datasets/Iris/iris.pyndb.gz", "Datasets/MNIST/mnist.pyndb.gz"]
names = ["boston_housing.pyndb.gz","fashion_mnist.pyndb.gz","iris.pyndb.gz","mnist.pyndb.gz"]
HOME = expanduser("~")
if not exists(f'{HOME}/.datasets'):
    mkdir(f'{HOME}/.datasets')

for file, name in zip(files, names):
    src_file = file
    dst_file = f"{HOME}/.datasets/{name}"
    shutil.copy(src_file, dst_file)

setup(
    name='DeeprAI-Datasets',
    version='0.0.2',
    author='Kieran Carter',
    description='A collection of datasets to use with DeeprAI',
    url="https://github.com/Deepr-ai/DeeprAI-Datasets",
    packages=find_packages(),
    package_data={"boston":["Datasets/BostonHousing/boston_housing.pyndb.gz"],
                  "fashion":["Datasets/FashionMNIST/fashion_mnist.pyndb.gz"],
                  "iris": ["Datasets/Iris/iris.pyndb.gz"],
                  "mnist": ["Datasets/MNIST/mnist.pyndb.gz"]},
    install_requires=[
        'numpy',
        'pyndb',
        'compress-pickle'
    ],
classifiers=["Programming Language :: Python :: 3",
             "License :: OSI Approved :: Apache Software License",
             "Operating System :: OS Independent",]
)