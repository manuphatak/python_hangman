# coding=utf-8
from functools import wraps

import click
from builtins import zip


def delete_game(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        finally:
            self.game = None

    return wrapper


class Presenter():
    def __init__(self, click=click):
        self.game = None
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
        else:
            yield '        |'

        yield '________|_'

    def status(self):
        misses = '{0:_<10s}'.format(''.join(self.game.misses))
        yield ''
        yield ''
        yield ''
        yield '{0:s}{1:s}'.format(' ' * 5, 'MISSES:')
        yield '{0:s}{1:s}'.format(' ' * 5, ' '.join(list(misses)))
        yield ''
        yield ''
        yield ''
        yield ''
        yield ''

    @delete_game
    def write(self, game=None, message=None, game_over=False, game_won=False):
        self.game = game
        self.click.clear()

        if message:
            self.click.secho('{0:45s}'.format(message), bold=True, fg='yellow')
        elif game_over:
            message = "YOU'RE AN IDIOT. THE ANSWER IS {0}".format(
                self.game.answer)
            self.click.secho('{0:45s}'.format(message), bold=True, fg='red')
        elif game_won:
            message = "YOU ARE SO COOL"
            self.click.secho('{0:45s}'.format(message), bold=True, fg='cyan')
        else:
            self.click.echo()

        self.click.secho('{0: ^45s}'.format('HANGMAN GAME'), bold=True,
                         underline=True)

        iterate_this = list(zip(self.picture(), self.status()))
        for picture, details in iterate_this:
            self.click.echo('{0:10s}{1:35s}'.format(picture, details))

        deliminator = '   ' if len(game.status) < 45 / 4 else '  '
        status = deliminator.join(list(game.status))
        self.click.echo()
        self.click.echo('{0: ^45s}'.format(status))

        return self

    def prompt(self):
        self.click.echo()
        self.click.secho('Dare to pick a letter: ', dim=True, bold=True)
        return self.click.getchar()

    def play_again_prompt(self):
        self.click.echo()
        return self.click.confirm('Double or nothings?')

    def goodbye(self):
        self.click.secho('Have a nice day!', bold=True, fg='green', blink=True)
        self.click.echo()
