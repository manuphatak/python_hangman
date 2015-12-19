# coding=utf-8
from functools import partial

from mock import Mock
from pytest import fixture


@fixture(autouse=True)
def setup(monkeypatch):
    from hangman.utils import GameOverNotificationComplete, FlashMessage

    def draw_board(_, message=FlashMessage()):
        if message.game_lost or message.game_won:
            raise GameOverNotificationComplete
        return 'View draws board'

    monkeypatch.setattr('hangman.view.draw_board', draw_board)
    monkeypatch.setattr('hangman.view.say_goodbye', lambda: 'Have a nice day!')
    monkeypatch.setattr('hangman.view.prompt_guess', lambda: 'A')
    monkeypatch.setattr('hangman.view.prompt_play_again', lambda: False)


@fixture(autouse=True)
def game():
    from hangman.model import Hangman

    return Hangman(answer='hangman')


@fixture
def flash():
    from hangman.utils import FlashMessage

    return FlashMessage()


@fixture
def run(game, flash):
    from hangman.controller import run

    return partial(run, game=game, flash=flash)


def test_setup():
    from hangman import view
    from hangman.model import Hangman

    assert view.draw_board(Hangman()) == 'View draws board'
    assert view.say_goodbye() == 'Have a nice day!'
    assert view.prompt_guess() == 'A'
    assert not view.prompt_play_again()


def test_game_lost(game, run, monkeypatch, flash):
    monkeypatch.setattr('hangman.view.prompt_guess', lambda: 'O')
    game.misses = list('BCDEFIJKL')

    assert run() == 'Have a nice day!'
    assert flash.game_lost is True


def test_game_won(game, run, flash):
    game.hits = list('HNGMN')

    assert run() == 'Have a nice day!'
    assert flash.game_won is True


def test_value_error(game, run, monkeypatch):
    monkeypatch.setattr('hangman.view.prompt_guess', Mock(side_effect=['1', 'A']))
    game.hits = list('HNGMN')

    assert run() == 'Have a nice day!'


def test_keyboard_interupt(run, monkeypatch):
    monkeypatch.setattr('hangman.view.prompt_guess', Mock(side_effect=KeyboardInterrupt))

    assert run() == 'Have a nice day!'


def test_game_finished(run, monkeypatch):
    monkeypatch.setattr('hangman.view.prompt_guess',
                        Mock(side_effect=['H', 'A', 'N', 'G', 'M', 'N', KeyboardInterrupt]))
    monkeypatch.setattr('hangman.view.prompt_play_again', Mock(side_effect=[True, False]))

    assert run() == 'Have a nice day!'
