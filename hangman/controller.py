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


# noinspection PyPep8Naming
def game_loop(game=Hangman(), flash=FlashMessage()):
    """
    Main game loop.

    :param hangman.model.Hangman game: Hangman game instance.
    :param hangman.utils.FlashMessage flash: FlashMessage utility
    :return:
    """
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
        except KeyboardInterrupt:
            return view.say_goodbye()
        except GameFinished:
            break

    if view.prompt_play_again():
        # reuse classes originally passed into function
        GameClass, FlashClass = game.__class__, flash.__class__

        return game_loop(game=GameClass(), flash=FlashClass())

    return view.say_goodbye()
