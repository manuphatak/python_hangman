# coding=utf-8
"""
Collection of words to choose from.
"""
from __future__ import absolute_import
from random import choice

__all__ = ['WordBank', 'FlashMessage']


class WordBank(object):
    WORDS = (
        'ATTEMPT', 'DOLL', 'ELLEN', 'FLOATING', 'PRIDE', 'HEADING', 'FILM', 'KIDS', 'MONKEY', 'LUNGS', 'HABIT', 'SPIN',
        'DISCUSSION', 'OFFICIAL', 'PHILADELPHIA', 'FACING', 'MARTIN', 'NORWAY', 'POLICEMAN', 'TOBACCO', 'VESSELS',
        'TALES', 'VAPOR', 'INDEPENDENT', 'COOKIES', 'WEALTH', 'PENNSYLVANIA', 'EXPLANATION', 'DAMAGE', 'OCCASIONALLY',
        'EXIST', 'SIMPLEST', 'PLATES', 'CANAL', 'NEIGHBORHOOD', 'PALACE', 'ADVICE', 'LABEL', 'DANNY', 'CLAWS', 'RUSH',
        'CHOSE', 'EGYPT', 'POETRY', 'BREEZE', 'WOLF', 'MANUFACTURING', 'OURSELVES', 'SCARED', 'ARRANGEMENT', 'POSSIBLY',
        'PROMISED', 'BRICK', 'ACRES', 'TREATED', 'SELECTION', 'POSITIVE', 'CONSTANTLY', 'SATISFIED', 'ZOO', 'CUSTOMS',
        'UNIVERSITY', 'FIREPLACE', 'SHALLOW', 'INSTANT', 'SALE', 'PRACTICAL', 'SILLY', 'SATELLITES', 'SHAKING', 'ROCKY',
        'SLOPE', 'CASEY', 'REMARKABLE', 'RUBBED', 'HAPPILY', 'MISSION', 'CAST', 'SHAKE', 'REQUIRE', 'DONKEY',
        'EXCHANGE', 'JANUARY', 'MOUNT', 'AUTUMN', 'SLIP', 'BORDER', 'LEE', 'MELTED', 'TRAP', 'SOLAR', 'RECALL',
        'MYSTERIOUS', 'SWUNG', 'CONTRAST', 'TOY', 'GRABBED', 'AUGUST', 'RELATIONSHIP', 'HUNTER', 'DEPTH', 'FOLKS',
        'DEEPLY', 'IMAGE', 'STIFF', 'RHYME', 'ILLINOIS', 'SPECIES', 'ADULT', 'FINEST', 'THUMB', 'SLIGHT', 'GRANDMOTHER',
        'SHOUT', 'HARRY', 'MATHEMATICS', 'MILL', 'ESSENTIAL', 'TUNE', 'FORT', 'COACH', 'NUTS', 'GARAGE', 'CALM',
        'MEMORY', 'SOAP')

    @classmethod
    def set(cls, *value):
        cls.WORDS = value

    @classmethod
    def get(cls):
        """
        Pick a word at random.

        :param [str] choices: List of words to choose from.
        :return str: Random word.
        """
        return choice(cls.WORDS)


class FlashMessage(object):
    message = ''
    game_over = False
    game_won = False
    game_answer = None

    def __call__(self, message):
        self.message = message

    def __str__(self):
        message, self.message = self.message, ''
        return str(message)

    def __bool__(self):
        return bool(self.message)

    def __eq__(self, other):
        return bool(self.message) == other
