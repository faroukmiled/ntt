# ntt

*This README describes ntt packaging*

## Create a virtual environment

On unix-like os, with standard [venv](https://docs.python.org/3.10/library/venv.html) module

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install --upgrade pip setuptools wheel
```

## Install pip-tools dependency management tool

[pip-tools](https://pypi.org/project/pip-tools/) is a tool which computes
dependencies and install packages.

[pipdeptree](https://github.com/tox-dev/pipdeptree) is optional. It is a
command-line tool that display dependency trees.

```bash
$ pip install pip-tools pipdeptree
```

## Get the ntt package

Clone this repository to get the ntt package.

## Compute dependencies

`pip-compile` will compute the dependencies from a `requirements.in` files that
specifies an [Editable install](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs)
of the ntt package.

```bash
$ pip-compile --resolver=backtracking requirements.in
```

The `requirements-dev.in` install the optional "dev" dependencies (`pytest`,
...) listed in `pyproject.toml`. You may add a linter, a formatter, a
documentation tool and its extensions, ...

```bash
$ pip-compile --resolver=backtracking requirements-dev.in
```

`pip-compile` will generate a `.txt` file with the same base name as the `.in`
file.

## Install ntt package with its optional dependencies

You probably want to install ntt with its optional "dev" dependencies. So once
the dependencies computed, you have to install them in your environment with
`pip-sync`.

```bash
$ pip-sync requirements-dev.txt
```

## Test your installation

Run the tests :

```bash
$ pytest tests
```

You can also run the example codes in `examples` :

```bash
$ cd examples
$ python simple_frame_extraction.py
```

## Build ntt package

You must have installed "dev" optional dependencies to have flit. Just run
`flit build`, this will create a source package ``.tar.gz`` and a wheel in the
``dist`` folder.

```bash
$ flit build
```


