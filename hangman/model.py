# coding=utf-8
"""
hangman.model
~~~~~~~~~~~~~

This module contains all of the game logic.
"""
from __future__ import absolute_import
import re
from collections import namedtuple
from hangman.utils import WordBank, GameOver, GameWon


class Hangman(object):
    """
    The hangman game object contains the logic for managing the status of the
    game and raising key game related events.

    >>> from hangman.model import Hangman
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
    """

    # CLASS PROPERTIES
    # -------------------------------------------------------------------

    MAX_TURNS = 10
    _re_answer_rules = re.compile('^[A-Z]{1,16}$')
    _re_guess_rules = re.compile('^[A-Z]$')
    _repr = namedtuple('hangman', ['status', 'misses', 'remaining_turns'])

    # CONSTRUCTOR
    # -------------------------------------------------------------------

    def __init__(self, answer=None):
        """
        Instantiate a new game. Populate answer if necessary.

        :param str answer: answer to game instance
        :raises: ValueError
        """
        if not answer:
            answer = WordBank.get()

        # Validate answer.
        if not self.is_valid_answer(answer):
            raise ValueError("Word must be letters A-Z")

        self.answer = answer.upper()
        self._misses = set()
        self._hits = set()

    # INSTANCE PROPERTIES
    # -------------------------------------------------------------------

    @property
    def misses(self):
        """
        Get list of misses.

        :rtype: [str]
        """
        return sorted(list(self._misses))

    @misses.setter
    def misses(self, value):
        """
        `self.misses` setter.  Check for game over.

        :param value: A single letter.
        :raises: GameOver
        """

        self._misses = set(value)
        if self.remaining_turns <= 0:
            raise GameOver

    @property
    def hits(self):
        """
        Get list of hits.

        :rtype: [str]
        """
        return sorted(list(self._hits))

    @hits.setter
    def hits(self, value):
        """
        `self.hits` setter.  Check for game won.

        :param value: A single letter.
        :raises: GameWon
        """

        self._hits = set(value)
        if self._hits == set(self.answer):
            raise GameWon

    @property
    def remaining_turns(self):
        """
        Calculate number of turns remaining.

        :return: Number of turns remaining.
        :rtype: int
        """
        return self.MAX_TURNS - len(self.misses)

    @property
    def status(self):
        """
        Build a string representation of status with letters for hits and _
        for unknowns.

        :return: game status as string
        :rtype: str
        """
        hits = self.hits

        def fill_in(letter):
            return letter if letter in hits else '_'

        return ''.join(fill_in(letter) for letter in self.answer)

    # PUBLIC API
    # -------------------------------------------------------------------

    def guess(self, letter):
        """
        Check if guess is a hit or miss.

        :param str letter: Letter to check
        :return: self
        :rtype: Hangman
        :raises: ValueError
        """
        # validate input
        if not self.is_valid_guess(letter):
            raise ValueError('Must be a letter A-Z')

        # add to hits or misses
        is_miss = letter.upper() not in self.answer
        if is_miss:
            self.add_miss(letter)
        else:
            self.add_hit(letter)

        return self

    # UTILITIES
    # -------------------------------------------------------------------

    def add_miss(self, value):
        """
        Add a miss to the model.  Check for game over.

        :param value: A single letter.
        :raises: GameOver
        """
        self._misses.add(value.upper())
        if self.remaining_turns <= 0:
            raise GameOver

    def add_hit(self, value):
        """
        Add a hit to the model.  Check for game won.

        :param value: A single letter.
        :raises: GameWon
        """
        self._hits.add(value.upper())
        if self._hits == set(self.answer):
            raise GameWon

    def is_valid_answer(self, word):
        """
        Validate answer.  Letters only.  Max:16

        :param str word: Word to validate.
        :return:
        :rtype: bool
        """
        word = str(word).upper()
        return not not self._re_answer_rules.search(word)

    def is_valid_guess(self, letter):
        """
        Validate guess.  Letters only.  Max:1

        :param str letter: Letter to validate
        :return:
        :rtype: bool
        """
        letter = str(letter).upper()
        return not not self._re_guess_rules.search(letter)

    def __repr__(self):
        """
        Build a human readable representation of self.

        :return: namedtuple with status, misses, and remaining_turns
        :rtype: namedtuple
        """

        return repr(self._repr(self.status, self.misses, self.remaining_turns))
