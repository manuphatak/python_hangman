# Hangman [![Build Status](https://travis-ci.org/bionikspoon/Hangman.svg?branch=develop)](https://travis-ci.org/bionikspoon/Hangman) [![Coverage Status](https://coveralls.io/repos/bionikspoon/Hangman/badge.svg?branch=develop)](https://coveralls.io/r/bionikspoon/Hangman?branch=develop) [![License](https://pypip.in/license/python_hangman/badge.svg)](https://pypi.python.org/pypi/python_hangman/) [![Downloads](https://pypip.in/download/python_hangman/badge.svg)](https://pypi.python.org/pypi/python_hangman/)

#### A Python TDD Experiment
My first python agnostic, tox tested, travis-backed, program!

Has **very high** unit test coverage, with passing tests on every version of python including PyPy.

**Compatibility** [![Supported Python versions](https://pypip.in/py_versions/python_hangman/badge.svg)](https://pypi.python.org/pypi/python_hangman/) 
- Python 2.6
- Python 2.7
- Python 3.2
- Python 3.3
- Python 3.4
- PyPy

![terminal](presents/hangman.jpg)

## Quick Start

```sh
mkvirtualenv hangman  # optional for venv users
pip install python_hangman
hangman 
```

#### Uninstall

```sh
pip uninstall python_hangman
```

#### Full Documentation

[https://hangman.readthedocs.org/](https://hangman.readthedocs.org/)

## Goal
Learning!  Python in this case.  I'm particularly interested in testing and Test Driven Development.  This was a TDD exercise.

Also, explored:
- Tox, test automation
- Travis CI
- Python version agnostic programming
- Setuptools
- Publishing on pip
- Coverage via coveralls
- Documentation with sphinx and ReadTheDocs

## Design
There are 3 main components that run the game:  [hangman.Hangman](hangman/hangman.py#L7), [hangman.Commander](hangman/hangman.py#L7), and [hangman.Presenter](hangman/presenter.py#L6)

The entirety of the game logic is contained in [hangman.Hangman](hangman/hangman.py#L7).  You could technically play the game in the python console by instantiating the class, submitting guesses with `Hangman.guess(self, letter)` and printing the game state.

For example:

```python
>>> from hangman.hangman import Hangman
>>> game = Hangman(answer='hangman')
>>> game.guess('a')
hangman(status='_A___A_', misses=[], remaining_turns=10)
>>> game.guess('n').guess('z').guess('e')
hangman(status='_AN__AN', misses=['Z', 'E'], remaining_turns=8)
>>> game.status, game.misses, game.remaining_turns
('_AN__AN', ['Z', 'E'], 8)
```

[hangman.Presenter](hangman/presenter.py#L6) is a simple presentation layer.  It handles printing the art to the console, and collecting input from the user  

The  [hangman.Commander](hangman/hangman.py#L7) is exactly that, the commander, the director, the maestro, the tour guide.  It guides you, the user, through the game.  It tells the presenter module what to print and what data to collect.  The commander updates the state of the game and handles game events. 

#### Design Reasoning

This design pattern was the right choice, because it offers a sensible separation between the game logic and presentation layer.  I did not know in advance how the game was going to interact with the user.  Curses was on the table, it still is.  But, following TDD, there needed to be an immediate working solution that could be swapped out in the future.  And that's what this design allows.  The presenter class can changed to any other presentation layer with out changing the game.

## Call Diagram
![Call Diagram](presents/charts/basic-1000-dot.png)
