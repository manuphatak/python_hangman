# coding=utf-8
"""
This module handles user interaction. Printing and prompting.
"""
from __future__ import absolute_import
# noinspection PyCompatibility
from builtins import zip
import click

from hangman.utils import FlashMessage, GameFinished


def partial_picture(remaining_turns):
    """
    Generator draw the iconic hangman game status.

    :return: Line of picture.
    """
    yield '    _____'
    yield '    |   |'
    if remaining_turns <= 9:
        yield '   (_)  |'
    else:
        yield '        |'

    if remaining_turns <= 5:
        yield '   \|/  |'
    elif remaining_turns <= 6:
        yield '   \|   |'
    elif remaining_turns <= 8:
        yield '    |   |'
    else:
        yield '        |'

    if remaining_turns <= 7:
        yield '    |   |'
    else:
        yield '        |'

    if remaining_turns <= 4:
        yield '    |   |'
    else:
        yield '        |'

    if remaining_turns <= 1:
        yield '  _/ \  |'
    elif remaining_turns <= 2:
        yield '   / \  |'
    elif remaining_turns <= 3:
        yield '   /    |'
    else:
        yield '        |'

    yield '________|_'


def partial_status(misses):
    """
    Draw game status.

    Generator Function.
    :return: Line of status.
    """
    misses = '{0:_<10s}'.format(''.join(misses))
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


def partial_message(flash):
    if flash:
        return click.secho('{0:45s}'.format(flash), bold=True, fg='yellow')
    if flash.game_over:
        message = "CAN'T EVEN WIN HANGMAN? THE ANSWER IS {0}".format(flash.game_answer)
        return click.secho('{0:45s}'.format(message), bold=True, fg='red')
    if flash.game_won:
        message = "YOU ARE SO COOL"
        return click.secho('{0:45s}'.format(message), bold=True, fg='cyan')

    click.echo()


def partial_header():
    return click.secho('{0: ^45s}'.format('HANGMAN GAME'), bold=True, underline=True)


def draw_board(game, message=FlashMessage()):
    """
    Present the game status with pictures.

    Clears the screen.
    Flashes any messages.
    Zip the two halves of the picture together.

    :param hangman.Hangman game: game instance
    :param hangman.utils.FlashMessage message: flash message
    :raises: hangman.utils.GameFinished
    :return: self
    """

    click.clear()

    partial_message(message)

    partial_header()

    merge_body = list(zip(partial_picture(game.remaining_turns), partial_status(game.misses)))
    for picture, details in merge_body:
        click.echo('{0:10s}{1:35s}'.format(picture, details))

    deliminator = '   ' if len(game.status) < 45 / 4 else '  '
    status = deliminator.join(list(game.status))
    click.echo()
    click.echo('{0: ^45s}'.format(status))

    if message.game_over or message.game_won:
        raise GameFinished


def prompt_guess():
    """
    Prompt user for a single keystroke.

    :return: a single letter
    """
    click.echo()
    click.secho('Dare to pick a letter: ', dim=True, bold=True)
    return click.getchar()


def prompt_play_again():
    """
    Prompt user to play again.

    :rtype: bool
    :return: bool response
    """
    click.echo('')
    return click.confirm('Double or nothings?')


def say_goodbye():
    """
    Write a goodbye message.
    """
    click.secho('Have a nice day!', bold=True, fg='green', blink=True)
    click.echo('')

# def delete_game(func):
#     """
#     Decorator.  Reset game state to prevent persistence.
#
#     :type func: __builtin__.function
#     :return: original function
#     """
#
#     @wraps(func)
#     def wrapper(self, *args, **kwargs):
#         try:
#             return func(self, *args, **kwargs)
#         finally:
#             self.game = None
#
#     return wrapper


# class Presenter(object):
#     """
#     Print and prompt.  This class is used by the commander to collect and
#     present data.  Makes extensive use of click's library.
#     """
#
#     def __init__(self, click=click):
#         """
#         Instantiate a new class. Should be treated like a singleton.
#
#         :type click: click
#         :return: self
#         """
#         self.game = None
#         self.click = click
