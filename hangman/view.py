# coding=utf-8
"""
hangman.view
~~~~~~~~~~~~

This module handles user interaction. Printing and prompting.
"""
from __future__ import absolute_import
# noinspection PyCompatibility
from builtins import zip
import click
from hangman.utils import FlashMessage, GameFinished


# DRAW COMPONENT BLOCK
# -------------------------------------------------------------------

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

    # setup
    click.clear()
    partial_picture = build_partial_picture(game.remaining_turns)
    partial_status = build_partial_status(game.misses)

    # print
    print_partial_message(message)
    print_partial_header()
    print_partial_body(partial_picture, partial_status)
    print_partial_footer(game.status)

    # raise to break game loop
    if message.game_over or message.game_won:
        raise GameFinished


def say_goodbye():
    """
    Write a goodbye message.
    """

    click.secho('Have a nice day!', bold=True, fg='green', blink=True)

    return print_spacer()


# PROMPT USER INPUT
# -------------------------------------------------------------------
def prompt_guess():
    """
    Prompt user for a single keystroke.

    :return: a single letter
    :raises: KeyboardInterrupt
    """

    print_spacer()

    click.secho('Dare to pick a letter: ', dim=True, bold=True)
    letter = click.getchar()
    if letter == '\x03':
        raise KeyboardInterrupt
    return letter


def prompt_play_again():
    """
    Prompt user to play again.

    :rtype: bool
    :return: bool response
    """
    print_spacer()

    return click.confirm('Double or nothings?')


# BUILD PARTIAL BLOCKS
# -------------------------------------------------------------------

def build_partial_picture(remaining_turns):
    """
    Generator. Draw the iconic hangman game status.

    :param int remaining_turns: Number of turns remaining.
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


def build_partial_status(misses_block):
    """
    Generator. Draw game status.

    :return: Line of status.
    """
    misses_block = ' '.join('{0:_<10s}'.format(''.join(misses_block)))
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

def print_partial_message(flash):
    if flash.game_over:
        message = "YOU LOSE! THE ANSWER IS {0}".format(flash.game_answer)
        return click.secho('{0:45s}'.format(message), bold=True, fg='red')
    if flash.game_won:
        message = "YOU ARE SO COOL"
        return click.secho('{0:45s}'.format(message), bold=True, fg='cyan')
    if flash.message:
        return click.secho('{0:45s}'.format(flash), bold=True, fg='yellow')

    return print_spacer()


def print_partial_header():
    return click.secho('{0: ^45s}'.format('HANGMAN GAME'), bold=True, underline=True)


def print_partial_body(picture, status):
    for line in zip(picture, status):
        click.echo('{0:10s}{1:35s}'.format(*line))


def print_partial_footer(game_status):
    space_between_letters = '   ' if len(game_status) < 45 / 4 else '  '
    formatted_game_status = space_between_letters.join(game_status)

    print_spacer()
    return click.echo('{0: ^45s}'.format(formatted_game_status))


def print_spacer():
    return click.echo()
