# coding=utf-8
"""
hangman.controller
~~~~~~~~~~~~~~~~~~

This module is responsible for guiding the user through the game.
"""
from __future__ import absolute_import

from hangman.utils import FlashMessage, GameOver, GameWon, GameFinished
from . import view
from .model import Hangman


def game_loop(game=Hangman(), flash=FlashMessage()):
    while True:
        try:
            view.draw_board(game, message=flash)
            letter = view.prompt_guess()
            game.guess(letter)
        except GameOver:
            flash.game_over = True
            flash.game_answer = game.answer
        except GameWon:
            flash.game_won = True
        except ValueError as msg:
            flash(msg)
        except GameFinished:
            break


def run(game=Hangman(), flash=FlashMessage()):
    """
    Run ``game_loop``, handle exit.

    Logic is separated from game_loop to cleanly avoid recursion limits.

    :param hangman.model.Hangman game: Hangman game instance.
    :param hangman.utils.FlashMessage flash: FlashMessage utility
    """

    # noinspection PyPep8Naming
    GameClass, FlashClass = game.__class__, flash.__class__
    while True:
        try:
            game_loop(game=game, flash=flash)
        except KeyboardInterrupt:
            # Exit immediately
            return view.say_goodbye()

        if not view.prompt_play_again():
            break

        # reuse classes passed in from arguments
        game, flash = GameClass(), FlashClass()

    return view.say_goodbye()
