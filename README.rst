=======
Hangman
=======

.. image:: https://badge.fury.io/py/python_hangman.svg
    :target: https://pypi.python.org/pypi/python_hangman/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/python_hangman.svg
    :target: https://pypi.python.org/pypi/python_hangman/
    :alt: Development Status

.. image:: https://travis-ci.org/bionikspoon/Hangman.svg?branch=develop
    :target: https://travis-ci.org/bionikspoon/Hangman?branch=develop
    :alt: Build Status

.. image:: https://coveralls.io/repos/bionikspoon/Hangman/badge.svg?branch=develop&service=github
    :target: https://coveralls.io/github/bionikspoon/Hangman?branch=develop
    :alt: Coverage Status

.. image:: https://readthedocs.org/projects/hangman/badge/?version=develop
    :target: https://hangman.readthedocs.org/en/develop/?badge=develop
    :alt: Documentation Status



**A Python TDD Experiment**

A python version agnostic, tox tested, travis-backed program! Documented and distributed.

Has **very high** unit test coverage, with passing tests on every relevant version of python including PyPy.

Features
--------

- Hangman!
- Idiomatic code.
- Thoroughly tested with very high coverage.
- Python version agnostic.
- Demonstrates MVC design out of the scope of web development.
- Documentation.

.. image:: https://cloud.githubusercontent.com/assets/5052422/11611464/00822c5c-9b95-11e5-9fcb-8c10fd9be7df.jpg
    :alt: Screenshot

Compatibility
-------------

.. image:: https://img.shields.io/badge/Python-2.6,_2.7,_3.3,_3.4,_3.5,_pypy-brightgreen.svg
    :target: https://pypi.python.org/pypi/python_hangman/
    :alt: Supported Python versions


- Python 2.6
- Python 2.7
- Python 3.3
- Python 3.4
- Python 3.5
- PyPy

Getting Started
---------------

At the command line either via easy_install or pip:

.. code-block:: shell

    $ mkvirtualenv hangman  # optional for venv users
    $ pip install python_hangman

    $ hangman


**Uninstall**

.. code-block:: shell

    $ pip uninstall python_hangman


Goal
----

2.0.0
~~~~~

**MVC pattern**.  The goal was to explicitely demonstrate an MVC pattern out of the scope of web development.

**Idiomatic code**.  In this overhaul there's a big emphasis on idiomatic code.  The code should be describing its' own intention with the clarity your grandmother could read.


1.0.0
~~~~~

Learning!  This was a Test Driven Development(TDD) exercise.

Also, explored:

- Tox, test automation
- Travis CI
- Python version agnostic programming
- Setuptools
- Publishing on pip
- Coverage via coveralls
- Documentation with sphinx and ReadTheDocs
- Cookiecutter development

Design
------

MVC Intro
~~~~~~~~~
This game roughly follows the **Model-View-Controller(MVC)** pattern.  In the latest overhaul, these roles have been explicitely named: :mod:`hangman.model`, :mod:`hangman.view`, :mod:`hangman.controller`.

Traditionally in MVC the ``controller`` is the focal point.  It tells the ``view`` what information to collect from the user and what to show.  It uses that information to communicate with the ``model``--also, the data persistence later--and determine the next step.  This Hangman MVC adheres to these principals

Model
~~~~~

The model is very simply the hangman game instance--:class:`hangman.model.Hangman`.  It's a class.  Every class should have "state" and the methods of that class should manage that state.  In this case, the "state" is the current "state of the game".  The public API are for manageing that state.

The entirety of the game logic is contained in :class:`hangman.model.Hangman`.  You could technically play the game in the python console by instantiating the class, submitting guesses with the method :meth:`hangman.model.Hangman.guess` and printing the game state.

For example:

.. code-block:: python

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


View
~~~~

:mod:`hangman.view` is a collection of stateless functions that represent the presentation layer.  When called these functions handles printing the art to the console, and collecting input from the user.

Controller
~~~~~~~~~~

In this program, the ``controller`` is actually the "game_loop"--:func:`hangman.controller.game_loop`.  I still think of it as a ``controller`` because the role it plays--communicating I/O from the view with the model-persistence layer.

The controller tells the view later what to print and what data to collect.  It uses that information update the state of the game (model) and handle game events.


Call Diagram
------------

.. image:: https://cloud.githubusercontent.com/assets/5052422/11611800/bfc9ec20-9ba5-11e5-9b18-95d361e7ba23.png
    :alt: Call Diagram


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `bionikspoon/cookiecutter-pypackage`_ forked from `audreyr/cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`bionikspoon/cookiecutter-pypackage`: https://github.com/bionikspoon/cookiecutter-pypackage
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
