# coding=utf-8
"""
This module is responsible for guiding the user through the game.
"""
from __future__ import absolute_import
from hangman.utils import FlashMessage, GameOver, GameWon, GameFinished
from . import view
from .hangman import Hangman


# class Commander(object):
#     """
#     The commander guides the user through the game, by telling the presenter
#     what information to collect and what data to show and updating the status
#     of the game.
#     """
#
#     def __init__(self, hangman=Hangman):
#         self.game = hangman()
#
#     @classmethod
#     def run(cls, hangman=Hangman):
#         """
#         Start the tour.
#
#         :param hangman: Hangman dependency injection.
#         :param presenter: Presenter dependence injection.
#         :return: An instance of self.
#         """
#         self = cls(hangman=hangman)
#         flash = None
#         play_again = False
#         while True:
#             view.draw_board(self.game, message=flash)
#             flash = None
#             guess = view.prompt_guess()
#             try:
#                 self.game.guess(guess)
#             except GameOver:
#                 view.draw_board(self.game, game_over=True)
#                 play_again = view.prompt_play_again()
#                 break
#             except GameWon:
#
#                 view.draw_board(self.game, game_won=True)
#                 play_again = view.prompt_play_again()
#                 break
#             except ValueError as e:
#                 flash = e
#                 continue
#         if play_again:
#             del self
#             cls.run(hangman=hangman)
#         else:
#             view.say_goodbye()
#             return self


def game_loop(game=None):
    game = game or Hangman()
    flash = FlashMessage()
    while True:
        view.draw_board(game, message=flash)
        guess = view.prompt_guess()

        try:
            game.guess(guess)
        except GameOver:
            flash.game_over = True
            flash.game_answer = game.answer
        except GameWon:
            flash.game_won = True
        except ValueError as msg:
            flash(msg)
        except GameFinished:
            break

    if view.prompt_play_again():
        return game_loop()

    return view.say_goodbye()


if __name__ == '__main__':
    game_loop()
