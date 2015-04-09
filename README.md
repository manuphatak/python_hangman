# TDD Python Hangman [![Build Status](https://travis-ci.org/bionikspoon/tdd_python_hangman.svg?branch=master)](https://travis-ci.org/bionikspoon/tdd_python_hangman)

My first multiversion, tox tested, travis-backed, program!

Has **~100%** unit test coverage, with passing tests on every version of python.

**Compatibility**
- Python 2.6
- Python 2.7
- Python 3.2
- Python 3.3
- Python 3.4
- PyPy

## Usage

```sh
git clone git@github.com:bionikspoon/tdd_python_hangman.git
cd tdd_python_hangman
mkvirtualenv hangman  # optional for venv users
pip install .
hangman 
```

#### Uninstall
```shell
rmvirtualenv hangman
```
or
```sh
workon hangman # for venv users
pip uninstall python-hangman
deactivate # for venv users
```
