#!/usr/bin/env python
# coding=utf-8
"""
==============
python_hangman
==============

A well tested, cli, python version-agnostic, multi-platform hangman game.
It's built following TDD principles and each component services a
sensibly distinct logical purpose.

"""
from __future__ import absolute_import
import logging

from ._compat import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())

__author__ = 'Manu Phatak'
__email__ = 'bionikspoon@gmail.com'
__version__ = '2.2.0'
