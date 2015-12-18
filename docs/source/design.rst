======
Design
======

MVC Intro
---------
This game roughly follows the **Model-View-Controller(MVC)** pattern.  In the latest overhaul, these roles have been explicitely named: :mod:`hangman.model`, :mod:`hangman.view`, :mod:`hangman.controller`.

Traditionally in MVC the ``controller`` is the focal point.  It tells the ``view`` what information to collect from the user and what to show.  It uses that information to communicate with the ``model``--also, the data persistence later--and determine the next step.  This Hangman MVC adheres to these principals

Model
-----

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
----

:mod:`hangman.view` is a collection of stateless functions that represent the presentation layer.  When called these functions handles printing the art to the console, and collecting input from the user.

Controller
----------

In this program, the ``controller`` is actually the "game_loop"--:func:`hangman.controller.game_loop`.  I still think of it as a ``controller`` because the role it plays--communicating I/O from the view with the model-persistence layer.

The controller tells the view later what to print and what data to collect.  It uses that information update the state of the game (model) and handle game events.
