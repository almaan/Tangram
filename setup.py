#!/usr/bin/env python3

import setuptools

with open("README.md","r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tangram",
    version="0.2.0",
    author="Tommaso Biancalani, Gabriele Scalia ",
    author_email="",
    description="Spatial alignment of single cell transcriptomic data. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/broadinstitute/Tangram",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: Tested on Mac OS and Linux",
    ],
    python_requires='>=3.7',
    install_requires=[
        "pip>=19.0.0",
        "torch>=1.4.0",
        "pandas>=1.1.0",
        "numpy>=1.19.1",
        "scipy>=1.5.2",
        "matplotlib>=3.0.0",
        "seaborn>=0.10.1",
        "jupyterlab>=2.2.6",
    ]
)



