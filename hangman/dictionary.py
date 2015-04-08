# coding=utf-8
from random import choice


class Dictionary(object):
    WORDS = ['ATTEMPT', 'DOLL', 'ELLEN', 'FLOATING', 'PRIDE', 'HEADING', 'FILM',
             'KIDS', 'MONKEY', 'LUNGS', 'HABIT', 'SPIN', 'DISCUSSION',
             'OFFICIAL', 'PHILADELPHIA', 'FACING', 'MARTIN', 'NORWAY',
             'POLICEMAN', 'TOBACCO', 'VESSELS', 'TALES', 'VAPOR', 'INDEPENDENT',
             'COOKIES', 'WEALTH', 'PENNSYLVANIA', 'EXPLANATION', 'DAMAGE',
             'OCCASIONALLY', 'EXIST', 'SIMPLEST', 'PLATES', 'CANAL',
             'NEIGHBORHOOD', 'PALACE', 'ADVICE', 'LABEL', 'DANNY', 'CLAWS',
             'RUSH', 'CHOSE', 'EGYPT', 'POETRY', 'BREEZE', 'WOLF',
             'MANUFACTURING', 'OURSELVES', 'SCARED', 'ARRANGEMENT', 'POSSIBLY',
             'PROMISED', 'BRICK', 'ACRES', 'TREATED', 'SELECTION', 'POSITIVE',
             'CONSTANTLY', 'SATISFIED', 'ZOO', 'CUSTOMS', 'UNIVERSITY',
             'FIREPLACE', 'SHALLOW', 'INSTANT', 'SALE', 'PRACTICAL', 'SILLY',
             'SATELLITES', 'SHAKING', 'ROCKY', 'SLOPE', 'CASEY', 'REMARKABLE',
             'RUBBED', 'HAPPILY', 'MISSION', 'CAST', 'SHAKE', 'REQUIRE',
             'DONKEY', 'EXCHANGE', 'JANUARY', 'MOUNT', 'AUTUMN', 'SLIP',
             'BORDER', 'LEE', 'MELTED', 'TRAP', 'SOLAR', 'RECALL', 'MYSTERIOUS',
             'SWUNG', 'CONTRAST', 'TOY', 'GRABBED', 'AUGUST', 'RELATIONSHIP',
             'HUNTER', 'DEPTH', 'FOLKS', 'DEEPLY', 'IMAGE', 'STIFF', 'RHYME',
             'ILLINOIS', 'SPECIES', 'ADULT', 'FINEST', 'THUMB', 'SLIGHT',
             'GRANDMOTHER', 'SHOUT', 'HARRY', 'MATHEMATICS', 'MILL',
             'ESSENTIAL', 'TUNE', 'FORT', 'COACH', 'NUTS', 'GARAGE', 'CALM',
             'MEMORY', 'SOAP']

    def __call__(self):
        return choice(self.WORDS)