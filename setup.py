#!/usr/bin/env python2
# coding: uft-8

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shellomock",
    version="0.0.1",
    author="Sergiienko Stanislav",
    author_email="ssergiienko.s@gmail.com",
    description="shellomock",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ssergiienko/shellomock",
    packages=setuptools.find_packages(where='src'),
    package_dir={"": "src"},
    extras_require={
        "tests": ["pytest"],
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
    ],
)
