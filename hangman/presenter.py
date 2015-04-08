# coding=utf-8
import sys

import click


hangman_base = """
    _____
    |   |
   (_)  |
   \|/  |
    |   |
    |   |
  _/ \  |
________|_
"""


class Presenter():
    game = None

    def __init__(self, game=None, out=sys.stdout, click=click):
        self.out = out
        self.game = game
        self.click = click

    def picture(self):
        turns = self.game.remaining_turns
        yield '    _____'
        yield '    |   |'
        if turns <= 9:
            yield '   (_)  |'
        else:
            yield '        |'

        if turns <= 5:
            yield '   \|/  |'
        elif turns <= 6:
            yield '   \|   |'
        elif turns <= 8:
            yield '    |   |'
        else:
            yield '        |'

        if turns <= 7:
            yield '    |   |'
        else:
            yield '        |'

        if turns <= 4:
            yield '    |   |'
        else:
            yield '        |'

        if turns <= 1:
            yield '  _/ \  |'
        elif turns <= 2:
            yield '   / \  |'
        elif turns <= 3:
            yield '   /    |'

        yield '________|_'

    def status(self):
        yield ''
        yield '{: ^50s}'.format('HANGMAN GAME')
        yield ''
        yield '{:s}{:s}'.format(' ' * 5, 'MISSES:')
        yield '{:s}{:s}'.format(' ' * 5, ' '.join(self.game.misses))
        yield ''
        yield ''
        yield ''
        yield ''
        yield ''

    @classmethod
    def write(cls, game, flash, *args, **kwargs):
        self = cls(game=game, *args, **kwargs)
        self.click.clear()
        if flash:
            self.click.secho('{:60s}'.format(flash), bold=True, fg='yellow')
            self.click.echo()

        try:
            iterate_this = zip(self.picture(), self.status(), xrange(10))
            for picture, details, i in iterate_this:
                self.click.echo('{:10s}{:50s}'.format(picture, details))
        except StopIteration:
            pass
        status = '   '.join(list(game.status))
        self.click.echo()
        self.click.echo('{: ^60s}'.format(status))

        return self

    @classmethod
    def prompt(cls, *args, **kwargs):
        self = cls(*args, **kwargs)
        self.click.echo()
        return raw_input('Dare to pick a letter: ')

