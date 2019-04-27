#!/bin/python3

from setuptools import find_packages, setup


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="pump",
    version="0.1.0",
    author='0sum',
    description='pumping tool for phyto',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('src')
)