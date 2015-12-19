# coding=utf-8
"""
hangman.controller
~~~~~~~~~~~~~~~~~~
"""
from __future__ import absolute_import

from hangman.utils import FlashMessage, GameLost, GameWon, GameOverNotificationComplete
from . import view
from .model import Hangman


def game_loop(game=Hangman(), flash=FlashMessage()):
    """
    Run a single game.

    :param hangman.model.Hangman game: Hangman game instance.
    :param hangman.utils.FlashMessage flash: FlashMessage utility
    """

    while True:
        try:
            # Draw -> prompt -> guess
            view.draw_board(game, message=flash)
            letter = view.prompt_guess()
            game.guess(letter)

        except GameLost:
            flash.game_lost = True
        except GameWon:
            flash.game_won = True
        except ValueError as msg:
            flash(msg)
        except GameOverNotificationComplete:  # raised by view, finished drawing
            break


# noinspection PyPep8Naming
def run(game=Hangman(), flash=FlashMessage()):
    """
    Run ``game_loop`` and handle exiting.

    Logic is separated from game_loop to cleanly avoid python recursion limits.

    :param hangman.model.Hangman game: Hangman game instance.
    :param hangman.utils.FlashMessage flash: FlashMessage utility
    """

    # setup, save classes for reuse
    GameClass, FlashClass = game.__class__, flash.__class__

    while True:
        try:
            game_loop(game=game, flash=flash)
        except KeyboardInterrupt:  # exit immediately
            break

        if not view.prompt_play_again():
            break

        # setup next game
        game, flash = GameClass(), FlashClass()

    return view.say_goodbye()
