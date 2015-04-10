# coding=utf-8
import click
import pytest
from mock import Mock
from builtins import map

from hangman import Presenter, Hangman

try:
    import __pypy__
except ImportError:
    __pypy__ = None


@pytest.fixture
def game():
    mock_game = Mock(spec=Hangman)
    mock_game.return_value = mock_game
    mock_game.misses = []
    mock_game.status = '_______'
    mock_game.answer = 'HANGMAN'
    return mock_game


@pytest.fixture
def presenter(monkeypatch):
    monkeypatch.setattr('click.getchar', lambda: 'A')
    monkeypatch.setattr('click.confirm', lambda _: True)
    return Presenter()


def test_mock_init(presenter):
    presenter.game = None
    presenter.click = click


def test_picture_10_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 10

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '        |', '        |', '        |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_9_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 9

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '        |', '        |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_8_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 8

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '    |   |', '        |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_7_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 7

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '    |   |', '    |   |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_6_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 6

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|   |', '    |   |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_5_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 5

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_4_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 4

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '    |   |', '        |', '________|_']
    assert actual == expected


def test_picture_3_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 3

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '    |   |', '   /    |', '________|_']
    assert actual == expected


def test_picture_2_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 2

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '    |   |', '   / \  |', '________|_']
    assert actual == expected


def test_picture_1_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 1

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '    |   |', '  _/ \  |', '________|_']
    assert actual == expected


def test_picture_0_turns(presenter, game):
    presenter.game = game
    presenter.game.remaining_turns = 0

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '    |   |', '  _/ \  |', '________|_']
    assert actual == expected


def test_status_0_misses_full(presenter, game):
    presenter.game = game
    presenter.game.misses = []
    actual = [line for line in presenter.status()]
    expected = ['', '', '', '     MISSES:', '     _ _ _ _ _ _ _ _ _ _', '', '',
                '', '', '']

    assert actual == expected


def test_status_2_misses(presenter, game):
    presenter.game = game
    presenter.game.misses = ['A', 'E']

    actual = [line for line in presenter.status()]
    expected = ['', '', '', '     MISSES:', '     A E _ _ _ _ _ _ _ _', '', '',
                '', '', '']

    assert set(actual[4].split(' ')) == set(expected[4].split(' '))


def test_status_10_misses(presenter, game):
    presenter.game = game
    presenter.game.misses = list('QWERTYASDF')

    actual = [line for line in presenter.status()]
    expected = ['', '', '', '     MISSES:', '     A E D F Q S R T W Y', '', '',
                '', '', '']

    assert set(actual[4].split(' ')) == set(expected[4].split(' '))


def test_write_output(game, capsys):
    expected = """
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
"""
    Presenter().write(game=game)
    out, err = capsys.readouterr()
    actual = [line.strip() for line in out.split('\n')]
    assert actual == list(map(str.strip, expected.split('\n')))
    assert err == ''


def test_flash_message(game, capsys):
    message = 'This test is a success'
    Presenter().write(game=game, message=message)
    out, err = capsys.readouterr()
    assert out.split('\n')[0] == '{0: <45}'.format(message)
    assert err == ''


def test_prompt_class_method(presenter):
    actual = presenter.prompt()
    assert actual is 'A'


def test_play_again_prompt_method_true(presenter):
    actual = presenter.play_again_prompt()
    assert actual is True


def test_goodbye_method(capsys, presenter):
    presenter.goodbye()
    out, err = capsys.readouterr()
    assert out == 'Have a nice day!\n\n'
    assert err == ''


def test_game_does_not_persist_between_calls(presenter, game, capsys):
    presenter.write(game=game)
    capsys.readouterr()

    assert presenter.game is None


def test_game_won(capsys, presenter, game):
    expected = 'YOU ARE SO COOL'

    presenter.write(game=game, game_won=True)
    out, err = capsys.readouterr()

    assert out.split('\n')[0].strip() == expected


def test_game_over(capsys, presenter, game):
    expected = "YOU'RE AN IDIOT. THE ANSWER IS HANGMAN"

    presenter.write(game=game, game_over=True)
    out, err = capsys.readouterr()

    assert out.split('\n')[0].strip() == expected