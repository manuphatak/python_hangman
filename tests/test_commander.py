# coding=utf-8

import pytest
from mock import Mock

from hangman.commander import Commander
from hangman.hangman import Hangman, GameOver, GameWon
from hangman.presenter import Presenter


@pytest.fixture
def presenter():
    mock = Mock(spec=Presenter)
    mock.return_value = mock
    mock.write.return_value = 'Presenter writes'
    mock.play_again_prompt.return_value = False
    mock.prompt.return_value = 'A'
    return mock


@pytest.fixture
def commander(presenter):
    commander = Commander(presenter=presenter())
    commander.game = Hangman(answer='hangman')
    return commander


def test_init(commander, presenter):
    assert commander.game.answer == Hangman('hangman').answer == 'HANGMAN'
    assert presenter.write() == 'Presenter writes'
    assert commander.presenter.write() == 'Presenter writes'


def test_game_over(presenter, capsys):
    # Hangman.guess = Mock(side_effect=GameOver)
    mock = Mock()
    mock.return_value = mock
    mock.guess.side_effect = GameOver
    Commander.run(hangman=mock, presenter=presenter())

    out, err = capsys.readouterr()

    assert out == ''


def test_game_won(presenter, capsys):
    mock = Mock()
    mock.return_value = mock
    mock.guess.side_effect = GameWon
    Commander.run(hangman=mock, presenter=presenter())

    out, err = capsys.readouterr()

    assert out == ''


def test_value_error(presenter, capsys, monkeypatch):
    mock = Mock()
    mock.return_value = mock
    mock.guess.side_effect = [ValueError('Test'), GameWon]
    Commander.run(hangman=mock, presenter=presenter())

    out, err = capsys.readouterr()

    assert out == ''
