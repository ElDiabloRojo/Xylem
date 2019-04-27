pump
========

pumping tool for xylem unit.

## Usage

Pass duration (seconds) and motor address list to activate pumping sequence.

Example command: 

```
$ pump --motor-list 1 2 --duration 600
```


## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:example/pgbackup`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`