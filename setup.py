from setuptools import setup, find_packages
from pathlib import Path
import shutil
import os

# Define dataset files relative to this script
DATASET_DIRS = {
    "BostonHousing": "Datasets/BostonHousing/boston_housing.pyndb.gz",
    "FashionMNIST": "Datasets/FashionMNIST/fashion_mnist.pyndb.gz",
    "Iris": "Datasets/Iris/iris.pyndb.gz",
    "MNIST": "Datasets/MNIST/mnist.pyndb.gz"
}

HOME = Path.home()
DATASET_HOME = HOME / ".datasets"

# Ensure ~/.datasets exists
DATASET_HOME.mkdir(exist_ok=True)

# Copy datasets into ~/.datasets
for name, rel_path in DATASET_DIRS.items():
    src_file = Path(__file__).parent / rel_path
    dst_file = DATASET_HOME / Path(rel_path).name

    try:
        if src_file.exists():
            shutil.copy2(src_file, dst_file)
            print(f"Copied {src_file} → {dst_file}")
        else:
            print(f"Warning: {src_file} not found, skipping.")
    except PermissionError:
        print(f"Permission denied while copying {src_file}, skipping.")
    except Exception as e:
        print(f"Error copying {src_file}: {e}")

# Setup configuration
setup(
    name='DeeprAI-Datasets',
    version='0.0.2',
    author='Kieran Carter',
    description='A collection of datasets to use with DeeprAI',
    url='https://github.com/Deepr-ai/DeeprAI-Datasets',
    packages=find_packages(),
    package_data={
        "DeeprAI_Datasets": list(DATASET_DIRS.values())
    },
    include_package_data=True,
    install_requires=[
        'numpy',
        'pyndb',
        'compress-pickle'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
