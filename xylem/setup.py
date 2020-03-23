from setuptools import setup

setup(
    name="xylem",
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        xylem=main:cli
    ''',
)
