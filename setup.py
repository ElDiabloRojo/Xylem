from setuptools import setup, find_packages

setup(
    name="xylem",
    version='0.1',
    package_dir={'': 'xylem'},
    packages=find_packages(where='xylem'),
    install_requires=[
        'Click',
        'boto',
    ],
    entry_points='''
        [console_scripts]
        xylem=main:cli
    ''',
)
