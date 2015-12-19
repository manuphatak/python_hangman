# coding=utf-8
"""
hangman.view
~~~~~~~~~~~~

View layer, printing and prompting.
"""
from __future__ import absolute_import

import click

from ._compat import zip
from .utils import FlashMessage, GameOverNotificationComplete


# DRAW COMPONENT BLOCK
# -------------------------------------------------------------------

def draw_board(game, message=FlashMessage()):
    """
    Present the game status with pictures.

    - Clears the screen.
    - Flashes any messages.
    - Zip the two halves of the picture together.

    .. code-block:: text

        +---------------------------------------------+
        |              message 45 x 1                 |
        +---------------------------------------------+
        |              title 45 x 1                   |
        +----------+----------------------------------+
        |          |                                  |
        |          |                                  |
        |          |                                  |
        |          |                                  |
        | picture  |             misses               |
        | 10 x 10  |             35 x 10              |
        |          |                                  |
        |          |                                  |
        |          |                                  |
        |          |                                  |
        +----------+----------------------------------+
        |              hits 45 x 1                    |
        +---------------------------------------------+
        Dare to pick a letter:
        _

    **Example output:**

    .. code-block:: text

                        HANGMAN GAME
            _____
            |   |
                |
                |      MISSES:
                |      _ _ _ _ _ _ _ _ _ _
                |
                |
        ________|_
                  _   _   _   _   _   _   _
        Dare to pick a letter:
        _


    :param hangman.Hangman game: game instance
    :param hangman.utils.FlashMessage message: flash message
    :raises: hangman.utils.GameOverNotificationComplete
    """

    # setup
    click.clear()
    partial_picture = build_partial_picture(game.remaining_turns)
    partial_misses = build_partial_misses(game.misses)

    # print
    print_partial_message(message, game.answer)
    print_partial_title()
    print_partial_body(partial_picture, partial_misses)
    print_partial_hits(game.status)

    # raise to break game loop
    if message.game_lost or message.game_won:
        raise GameOverNotificationComplete


def say_goodbye():
    """Write a goodbye message."""

    click.secho('Have a nice day!', bold=True, fg='green', blink=True)

    return print_spacer()


# PROMPT USER INPUT
# -------------------------------------------------------------------
def prompt_guess():
    """Get a single letter."""

    print_spacer()

    click.secho('Dare to pick a letter: ', dim=True, bold=True)
    letter = click.getchar()

    # \x03 = ctrl+c, \x04 = ctrl+d
    if letter in ['\x03', '\x04']:
        raise KeyboardInterrupt
    return letter


def prompt_play_again():
    """Prompt user to play again."""

    print_spacer()
    return click.confirm('Double or nothings?')


# BUILD PARTIAL BLOCKS
# -------------------------------------------------------------------

def build_partial_picture(remaining_turns):
    """Generator, build the iconic hangman game status."""

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

    if remaining_turns <= 0:
        yield '  _/ \_ |'
    elif remaining_turns <= 1:
        yield '  _/ \  |'
    elif remaining_turns <= 2:
        yield '   / \  |'
    elif remaining_turns <= 3:
        yield '   /    |'
    else:
        yield '        |'

    yield '________|_'


def build_partial_misses(game_misses):
    """Generator, build game misses block."""

    misses_block = ' '.join('{0:_<10s}'.format(''.join(game_misses)))
    yield ''
    yield ''
    yield ''
    yield '{0:s}{1:s}'.format(' ' * 5, 'MISSES:')
    yield '{0:s}{1:s}'.format(' ' * 5, misses_block)
    yield ''
    yield ''
    yield ''
    yield ''
    yield ''


# PRINT PARTIAL BLOCKS
# -------------------------------------------------------------------

def print_partial_message(flash, answer):
    if flash.game_lost:
        message = "YOU LOSE! THE ANSWER IS {0}".format(answer)
        return click.secho('{0:45s}'.format(message), bold=True, fg='red')

    if flash.game_won:
        message = "YOU ARE SO COOL"
        return click.secho('{0:45s}'.format(message), bold=True, fg='cyan')

    if flash.message:
        return click.secho('{0:45s}'.format(flash), bold=True, fg='yellow')

    return print_spacer()


def print_partial_title():
    return click.secho('{0: ^45s}'.format('HANGMAN GAME'), bold=True, underline=True)


def print_partial_body(picture, status):
    for line in zip(picture, status):
        click.echo('{0:10s}{1:35s}'.format(*line))


def print_partial_hits(game_status):
    # Dynamically space hits to fill line
    space_between_letters = '   ' if len(game_status) < 45 / 4 else '  '
    formatted_game_status = space_between_letters.join(game_status)

    print_spacer()
    return click.echo('{0: ^45s}'.format(formatted_game_status))


def print_spacer():
    """Print empty line"""
    return click.echo()
