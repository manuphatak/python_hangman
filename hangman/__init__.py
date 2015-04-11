# coding=utf-8
"""
    hangman.__init__ module
    =======================

    A well tested, cli, python version-agnostic, multi-platform hangman game.
    It's built following TDD principles and each component services a
    sensibly distinct logical purpose.

"""
__version__ = '1.2.3'

from .dictionary import Dictionary
from .hangman import Hangman, GameOver, GameWon
from .presenter import Presenter
from .commander import Commander