import sys

from setuptools import setup, find_packages

requires = ["click", "boto"]
tests_requires = ["pytest", "pytest-cache", "pytest-cov"]
lint_requires = ["flake8", "black"]
dev_requires = ["bumpversion"] + requires + tests_requires + lint_requires


setup(

    name="xylem",
    version="0.1",
    description="",
    long_description="\n\n".join([open("README.rst").read()]),
    license="MIT",
    author="ElDiabloRojo",
    author_email="holdens.uk@googlemail.com",
    package_dir={'': 'xylem'},
    packages=find_packages(where='xylem'),
    install_requires=requires,
    entry_points={
        "console_scripts": [
            "xylem = cli:cli"
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    extras_require={"test": tests_requires, "dev": dev_requires, "lint": lint_requires},
)
