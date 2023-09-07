# Ape Notebook

Instantiate a Jupyter Notebook with Ape!

## Dependencies

- [python3](https://www.python.org/downloads) version 3.8 up to 3.11.

## Installation

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-notebook
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-notebook.git
cd ape-notebook
python3 setup.py install
```

## Quick Usage

Runs a notebook server:

```bash
ape notebook
```

`notebook >=7` has an outstanding issue at launch that can be [resolved](https://github.com/jupyter/notebook/issues/6974#issuecomment-1675394990)
by running in your environment

```bash
jupyter lab build
```

## Development

This project is in development and should be considered a beta.
Things might not be in their final state and breaking changes may occur.
Comments, questions, criticisms and pull requests are welcomed.

## License

This project is licensed under the [Apache 2.0](LICENSE).
