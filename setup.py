from setuptools import setup
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
    dst_file = name
    shutil.move(src_file, dst_file)

setup(
    name='DeeprAI-Datasets',
    version='0.0.1',
    author='Kieran Carter',
    description='A collection of datasets to use with DeeprAI',
    url="https://github.com/Deepr-ai/DeeprAI-Datasets",
    packages=["Datasets"],
    install_requires=[
        'numpy',
        'pyndb',
        'compress-pickle'
    ],
classifiers=["Programming Language :: Python :: 3",
             "License :: OSI Approved :: Apache Software License",
             "Operating System :: OS Independent",]
)