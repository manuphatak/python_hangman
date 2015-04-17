==============
Python Hangman
==============
.. image:: https://pypip.in/status/python-hangman/badge.svg
    :target: https://pypi.python.org/pypi/python_hangman/
    :alt: Development Status

.. image:: https://travis-ci.org/bionikspoon/Hangman.svg?branch=develop
    :target: https://travis-ci.org/bionikspoon/Hangman

.. image:: https://pypip.in/version/python-hangman/badge.svg?branch=develop
    :target: https://pypi.python.org/pypi/python_hangman?branch=develop

.. image:: https://coveralls.io/repos/bionikspoon/Hangman/badge.svg?branch=develop
    :target: https://coveralls.io/r/bionikspoon/Hangman?branch=develop

.. image:: https://readthedocs.org/projects/hangman/badge/?version=develop
    :target: https://hangman.readthedocs.org
    :alt: Documentation Status


**A Python TDD Experiment**

A python version agnostic, tox tested, travis-backed program! Documented and distributed.

Has **very high** unit test coverage, with passing tests on every version of python including PyPy.

Features
--------

TODO

.. image:: assets/hangman.jpg
    :alt: Documentation Status

Compatibility
-------------

.. image:: https://pypip.in/py_versions/python-hangman/badge.svg
    :target: https://pypi.python.org/pypi/python_hangman/
    :alt: Supported Python versions

.. image:: https://pypip.in/implementation/python-hangman/badge.svg
    :target: https://pypi.python.org/pypi/python_hangman/
    :alt: Supported Python implementations

- Python 2.6
- Python 2.7
- Python 3.2
- Python 3.3
- Python 3.4
- PyPy

Getting Started
---------------

At the command line either via easy_install or pip:

.. code-block:: sh

    mkvirtualenv hangman  # optional for venv users
    pip install python_hangman

    hangman


**Uninstall**

.. code-block:: shell

    $ pip uninstall python_hangman


Goal
----

Learning!  Python in this case.  I'm particularly interested in testing and Test Driven Development.  This was a TDD exercise.

Also, explored:

- Tox, test automation
- Travis CI
- Python version agnostic programming
- Setuptools
- Publishing on pip
- Coverage via coveralls
- Documentation with sphinx and ReadTheDocs

Design
------

There are 3 main components that run the game:  :py:class:`hangman.Hangman`,  :py:class:`hangman.Commander`, and :py:class:`hangman.Presenter`

The entirety of the game logic is contained in :py:class:`hangman.Hangman`.  You could technically play the game in the python console by instantiating the class, submitting guesses with `Hangman.guess(self, letter)` and printing the game state.

For example:

.. code-block:: python

    >>> from hangman.hangman import Hangman
    >>> game = Hangman(answer='hangman')
    >>> game.guess('a')
    hangman(status='_A___A_', misses=[], remaining_turns=10)

    >>> game.guess('n').guess('z').guess('e')
    hangman(status='_AN__AN', misses=['Z', 'E'], remaining_turns=8)

    >>> game.status, game.misses, game.remaining_turns
    ('_AN__AN', ['Z', 'E'], 8)

:py:class:`hangman.Presenter` is a simple presentation layer.  It handles printing the art to the console, and collecting input from the user

The  :py:class:`hangman.Commander` is exactly that, the commander, the director, the maestro, the tour guide.  It guides you, the user, through the game.  It tells the presenter module what to print and what data to collect.  The commander updates the state of the game and handles game events.

Design Reasoning
----------------

This design pattern was the right choice, because it offers a sensible separation between the game logic and presentation layer.  I did not know in advance how the game was going to interact with the user.  Curses was on the table, it still is.  But, following TDD, there needed to be an immediate working solution that could be swapped out in the future.  And that's what this design allows.  The presenter class can changed to any other presentation layer with out changing the game.

Call Diagram
------------

.. image:: assets/charts/basic-1000-dot.png
    :alt: Call Diagram
