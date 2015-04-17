# coding=utf-8
"""
    This module handles user interaction. Printing and prompting.
"""
from functools import wraps

import click
from builtins import zip


def delete_game(func):
    """
    Decorator.  Reset game state to prevent persistence.

    :type func: __builtin__.function
    :return: original function
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        finally:
            self.game = None

    return wrapper


class Presenter():
    """
    Print and prompt.  This class is used by the commander to collect and
    present data.  Makes extensive use of click's library.
    """

    def __init__(self, click=click):
        """
        Instantiate a new class. Should be treated like a singleton.

        :type click: click
        :return: self
        """
        self.game = None
        self.click = click

    def picture(self):
        """
        Draw the iconic hangman game status.

        Generator function.
        :return: Line of picture.
        """
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
        """
        Draw game status.

        Generator Function.
        :return: Line of status.
        """
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
        """
        Present the game status with pictures.

        Clears the screen.
        Flashes any messages.
        Zip the two halves of the picture together.

        :param hangman.Hangman game: game instance
        :param message: flash message
        :param bool game_over: GameOver has been raised
        :param bool game_won: GameWon has been raised
        :return: self
        """

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
        """
        Prompt user for a single keystroke.

        :return: a single letter
        """
        self.click.echo()
        self.click.secho('Dare to pick a letter: ', dim=True, bold=True)
        return self.click.getchar()

    def play_again_prompt(self):
        """
        Prompt user to play again.

        :rtype: bool
        :return: bool response
        """
        self.click.echo('')
        return self.click.confirm('Double or nothings?')

    def goodbye(self):
        """
        Write a goodbye message.
        """
        self.click.secho('Have a nice day!', bold=True, fg='green', blink=True)
        self.click.echo('')
