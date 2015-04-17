#!/usr/bin/env python
# coding=utf-8
"""
==============
Python Hangman
==============

A well tested, cli, python version-agnostic, multi-platform hangman game.
It's built following TDD principles and each component services a
sensibly distinct logical purpose.

"""

__author__ = 'Manu Phatak'
__email__ = 'bionikspoon@gmail.com'
__version__ = '1.3.1'


from .dictionary import Dictionary
from .hangman import Hangman, GameOver, GameWon
from .presenter import Presenter
from .commander import Commander