# coding=utf-8
import re


class Hangman(object):
    MAX_TURNS = 10

    def __init__(self, answer=None):
        if not self.valid_answer(answer):
            raise ValueError

        self.answer = answer.upper()
        self._misses = set()
        self._hits = set()


    @staticmethod
    def valid_answer(text):
        return re.compile('^[a-z]{1,16}$', re.I).search(str(text))

    def guess(self, letter):
        valid_guess = re.compile('^[a-z]$', re.I).search(str(letter))

        if not valid_guess:
            raise ValueError

        is_miss = letter.upper() not in self.answer

        if is_miss:
            self.misses = letter
        else:
            self.hits = letter

        return self

    @property
    def misses(self):
        return list(self._misses)

    @misses.setter
    def misses(self, value):
        self._misses.add(value.upper())
        if self.remaining_turns <= 0:
            raise GameOver

    @property
    def hits(self):
        return list(self._hits)

    @hits.setter
    def hits(self, value):
        self._hits.add(value.upper())
        if self._hits == set(self.answer):
            raise GameWon

    @property
    def remaining_turns(self):
        return self.MAX_TURNS - len(self.misses)

    @property
    def status(self):
        result = [letter if letter in self.hits else '_' for letter in
                  self.answer]

        return ''.join(result)


class GameWon(Exception):
    pass


class GameOver(Exception):
    pass