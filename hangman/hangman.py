# coding=utf-8
"""
    This module contains all of the game logic.
"""
from collections import namedtuple
import re

from . import Dictionary


class Hangman(object):
    """
    The hangman game object contains the logic for managing the status of the
    game and raising key game related events.

    >>> from hangman.hangman import Hangman
    >>> game = Hangman(answer='hangman')
    >>> game.guess('a')
    hangman(status='_A___A_', misses=[], remaining_turns=10)
    >>> game.guess('n').guess('z').guess('e')
    hangman(status='_AN__AN', misses=['Z', 'E'], remaining_turns=8)
    >>> game.status, game.misses, game.remaining_turns
    ('_AN__AN', ['Z', 'E'], 8)
    """
    MAX_TURNS = 10

    def __init__(self, answer=None, dictionary=Dictionary):
        """
        Instantiate a new game. Populate answer if necessary.

        :param str answer: answer to game instance
        :param hangman.Dictionary dictionary: class to generate answer
        :return: self
        """
        if not answer:
            answer = dictionary()()

        # Validate answer.
        if not self.valid_answer(answer):
            raise ValueError("Word must be letters A-Z")

        self.answer = answer.upper()
        self._misses = set()
        self._hits = set()

    def __repr__(self):
        """
        Build a human readable representation of self.

        :return: namedtuple with status, misses, and remaining_turns
        :rtype: namedtuple
        """
        return repr(namedtuple('hangman',
                               ['status', 'misses', 'remaining_turns'])._make(
            (self.status, self.misses, self.remaining_turns)))

    @staticmethod
    def valid_answer(word):
        """
        Validate word against game rules.  Letters only.  Max:16

        :param str word: letters only, max 16, case insensitive
        :return: true if valid
        :rtype: bool
        """
        return bool(re.compile('^[a-z]{1,16}$', re.I).search(str(word)))

    def guess(self, letter):
        """
        Validate guess against game rules.  Add guess to hit or miss.

        :param str letter: Any letter a-Z.  Length exactly 1
        :return: self
        """
        valid_guess = re.compile('^[a-z]$', re.I).search(str(letter))

        if not valid_guess:
            raise ValueError('Must be a letter A-Z')

        is_miss = letter.upper() not in self.answer

        if is_miss:
            self.misses = letter
        else:
            self.hits = letter

        return self

    @property
    def misses(self):
        """
        Get misses.

        :rtype list
        """
        return list(self._misses)

    @misses.setter
    def misses(self, value):
        """
        Set misses.  Check for game over.

        :param value: A single letter.
        :raises: GameOver
        """
        self._misses.add(value.upper())
        if self.remaining_turns <= 0:
            raise GameOver

    @property
    def hits(self):
        """
        Get hits.

        :rtype: list
        :return:
        """
        return list(self._hits)

    @hits.setter
    def hits(self, value):
        """
        Set hits.  Check for game won.

        :param value: A single letter.
        :raises: GameWon
        """
        self._hits.add(value.upper())
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
        result = [letter if letter in self.hits else '_' for letter in
                  self.answer]

        return ''.join(result)


class GameWon(Exception):
    """
    Indicate conditions for winning have been met.
    """


class GameOver(Exception):
    """
    Indicate conditions for losing have been met.
    """