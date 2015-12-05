# coding=utf-8
from functools import partial

import pytest
from mock import Mock

from hangman.controller import game_loop
from hangman.hangman import Hangman, GameOver, GameWon


@pytest.fixture
def view():
    mock = Mock()
    mock.return_value = mock
    mock.draw_board.return_value = 'View writes'
    mock.prompt_play_again.return_value = False
    mock.prompt_guess.return_value = 'A'
    return mock


# @pytest.fixture
# def game_loop():
#     from hangman.controller import game_loop
#
#     game = Hangman(answer='hangman')
#
#     return partial(game_loop, game=game)


# def test_init(game_loop, view):
#     assert controller.game.answer == Hangman('hangman').answer == 'HANGMAN'
#     assert view.write() == 'Presenter writes'
#     assert controller.view.write() == 'Presenter writes'


# def test_game_over(capsys):
#     # Hangman.guess = Mock(side_effect=GameOver)
#     mock = Mock()
#     mock.guess.side_effect = GameOver
#     game_loop(game=mock)
#
#     out, err = capsys.readouterr()
#
#     assert out == ''
#
#
# def test_game_won( capsys):
#     mock = Mock()
#     mock.return_value = mock
#     mock.guess.side_effect = GameWon
#     Commander.run(hangman=mock, )
#
#     out, err = capsys.readouterr()
#
#     assert out == ''
#
#
# def test_value_error( capsys):
#     mock = Mock()
#     mock.return_value = mock
#     mock.guess.side_effect = [ValueError('Test'), GameWon]
#     Commander.run(hangman=mock, )
#
#     out, err = capsys.readouterr()
#
#     assert out == ''
