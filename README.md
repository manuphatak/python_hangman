python\_hangman
===============

[![Github Downloads](https://img.shields.io/github/downloads/bionikspoon/python_hangman/total.svg)](https://github.com/bionikspoon/python_hangman)

[![Latest Version](https://badge.fury.io/py/python_hangman.svg)](https://pypi.python.org/pypi/python_hangman/)

[![Development Status](https://img.shields.io/pypi/status/python_hangman.svg)](https://pypi.python.org/pypi/python_hangman/)

[![Build Status](https://travis-ci.org/bionikspoon/python_hangman.svg?branch=develop)](https://travis-ci.org/bionikspoon/python_hangman?branch=develop)

[![Coverage Status](https://coveralls.io/repos/bionikspoon/python_hangman/badge.svg?branch=develop)](https://coveralls.io/github/bionikspoon/python_hangman?branch=develop&service=github)

[![Documentation Status](https://readthedocs.org/projects/python_hangman/badge/?version=develop)](https://python_hangman.readthedocs.org/en/develop/?badge=develop)

**A Python TDD Experiment**

A python version agnostic, tox tested, travis-backed program! Documented and distributed.

Has **very high** unit test coverage, with passing tests on every relevant version of python including PyPy.

Features
--------

-   Free software: MIT license
-   Documentation: <https://python_hangman.readthedocs.org>.
-   Hangman!
-   Idiomatic code.
-   Thoroughly tested with very high coverage.
-   Python version agnostic.
-   Demonstrates MVC design out of the scope of web development.
-   Documentation.

![Screenshot](https://cloud.githubusercontent.com/assets/5052422/11611464/00822c5c-9b95-11e5-9fcb-8c10fd9be7df.jpg)

Compatibility
-------------

[![Supported Python versions](https://img.shields.io/badge/Python-2.6,_2.7,_3.3,_3.4,_3.5,_pypy-brightgreen.svg)](https://pypi.python.org/pypi/python_hangman/)

-   Python 2.6
-   Python 2.7
-   Python 3.3
-   Python 3.4
-   Python 3.5
-   PyPy

Installation
============

Getting Started
---------------

At the command line either via easy\_install or pip

``` sourceCode
$ mkvirtualenv hangman  # optional for venv users
$ pip install python_hangman

$ hangman
```

**Uninstall**

``` sourceCode
$ pip uninstall python_hangman
```

Goals
=====

### 2.0.0

**MVC pattern**. The goal was to explicitely demonstrate an MVC pattern out of the scope of web development.

**Idiomatic code**. In this overhaul there's a big emphasis on idiomatic code. The code should be describing its' own intention with the clarity your grandmother could read.

### 1.0.0

Learning! This was a Test Driven Development(TDD) exercise.

Also, explored:

-   Tox, test automation
-   Travis CI
-   Python version agnostic programming
-   Setuptools
-   Publishing on pip
-   Coverage via coveralls
-   Documentation with sphinx and ReadTheDocs
-   Cookiecutter development

Design
======

MVC Intro
---------

This game roughly follows the **Model-View-Controller(MVC)** pattern. In the latest overhaul, these roles have been explicitely named: `hangman.model`, `hangman.view`, `hangman.controller`.

Traditionally in MVC the `controller` is the focal point. It tells the `view` what information to collect from the user and what to show. It uses that information to communicate with the `model`--also, the data persistence later--and determine the next step. This Hangman MVC adheres to these principals

Model
-----

The model is very simply the hangman game instance--`hangman.model.Hangman`. It's a class. Every class should have "state" and the methods of that class should manage that state. In this case, the "state" is the current "state of the game". The public API are for manageing that state.

The entirety of the game logic is contained in `hangman.model.Hangman`. You could technically play the game in the python console by instantiating the class, submitting guesses with the method `hangman.model.Hangman.guess` and printing the game state.

For example:

``` sourceCode
>>> from hangman.hangman import Hangman
>>> game = Hangman(answer='hangman')
>>> game.guess('a')
hangman(status='_A___A_', misses=[], remaining_turns=10)

>>> game.guess('n').guess('z').guess('e')
hangman(status='_AN__AN', misses=['E', 'Z'], remaining_turns=8)

>>> game.status
'_AN__AN'

>>> game.misses
['E', 'Z']

>>> game.remaining_turns
8
```

View
----

`hangman.view` is a collection of stateless functions that represent the presentation layer. When called these functions handles printing the art to the console, and collecting input from the user.

Controller
----------

In this program, the `controller` is actually the "game\_loop"--`hangman.controller.game_loop`. I still think of it as a `controller` because the role it plays--communicating I/O from the view with the model-persistence layer.

The controller tells the view later what to print and what data to collect. It uses that information update the state of the game (model) and handle game events.

Call Diagram
------------

![Call Diagram](https://cloud.githubusercontent.com/assets/5052422/11611800/bfc9ec20-9ba5-11e5-9b18-95d361e7ba23.png)

Credits
-------

Tools used in rendering this package:

-   [Cookiecutter](https://github.com/audreyr/cookiecutter)
-   [bionikspoon/cookiecutter-pypackage](https://github.com/bionikspoon/cookiecutter-pypackage) forked from [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)

