#!/usr/bin/env python
# coding=utf-8
"""
==============
python_hangman
==============

A well tested, cli, python version-agnostic, multi-platform hangman game. It's built following a TDD workflow and a
MVC design pattern. Each component services a sensibly distinct logical purpose.  Python Hangman is a version
agnostic, tox tested, travis-backed program! Documented and distributed.

"""
from __future__ import absolute_import

import logging

from ._compat import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())

__author__ = 'Manu Phatak'
__email__ = 'bionikspoon@gmail.com'
__version__ = '2.2.2'
