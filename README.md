# Ape Notebook

Instantiate a Jupyter Notebook with Ape!

## Dependencies

* [python3](https://www.python.org/downloads) version 3.7 or greater, python3-dev

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

### Install All 3rd Party Packages

```bash
pip install -e .
```

### Install Any Ape Plugins
Just an example, we install infura here

```bash
ape plugins install infura
```

### Create Your Ape Kernel
NOTE: This will be added to the CLI in the future

```bash
export WEB3_INFURA_PROJECT_ID=<your infura project ID>
ipython kernel install --name "ape" --user
```

### Start Up Your Notebook
```bash
ape notebook
```


## Development

This project is in development and should be considered a beta.
Things might not be in their final state and breaking changes may occur.
Comments, questions, criticisms and pull requests are welcomed.

## License

This project is licensed under the [Apache 2.0](LICENSE).
