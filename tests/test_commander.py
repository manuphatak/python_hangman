# coding=utf-8
from mock import Mock
import pytest
from hangman import Hangman, Presenter, Commander, GameOver, GameWon


@pytest.fixture
def hangman():
    mock = Mock(spec=Hangman)
    mock.return_value = mock
    mock.answer = 'HANGMAN'
    return mock


@pytest.fixture
def presenter():
    mock = Mock(spec=Presenter)
    mock.return_value = mock
    mock.write.return_value = 'Presenter writes'
    mock.play_again_prompt.return_value = False
    mock.prompt.return_value = 'A'
    return mock


@pytest.fixture
def commander(hangman=hangman, presenter=presenter):
    commander = Commander(hangman=hangman, presenter=presenter())
    return commander


def test_init(commander, hangman, presenter):
    assert commander.game.answer == hangman().answer == 'HANGMAN'
    assert presenter.write() == 'Presenter writes'
    assert commander.Presenter.write() == 'Presenter writes'


def test_game_over(hangman, presenter, capsys):
    hangman.guess.side_effect = GameOver
    Commander.run(hangman=hangman, presenter=presenter())

    out, err = capsys.readouterr()

    assert out == ''


def test_game_won(hangman, presenter, capsys):
    hangman.guess.side_effect = GameWon
    Commander.run(hangman=hangman, presenter=presenter())

    out, err = capsys.readouterr()

    assert out == ''


def test_value_error(hangman, presenter, capsys):
    hangman.guess.side_effect = [ValueError, GameWon]
    Commander.run(hangman=hangman, presenter=presenter())

    out, err = capsys.readouterr()

    assert out == ''

