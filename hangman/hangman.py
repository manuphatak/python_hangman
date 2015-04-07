# coding=utf-8
class Hangman(object):
    def __init__(self, answer=None):
        self.answer = answer.upper()
        self.misses = []
        self.remaining_turns = 10
        self.status = '_' * len(answer)

    def guess(self, letter):
        miss = True

        if miss:
            self.remaining_turns -= 1

        self.misses.append(letter.upper())

        return self