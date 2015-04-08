# coding=utf-8
import sys

import pytest

from mock import Mock

from hangman import Presenter, Hangman
from builtins import map
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
    return mock_game


@pytest.fixture
def click():
    import click

    mock_click = Mock(spec=click)
    mock_click.return_value = mock_click
    mock_click.confirm.return_value = True
    mock_click.getchar.return_value = 'A'
    return mock_click


@pytest.fixture
def presenter(game, click):
    return Presenter(game=game, click=click)


def test_mock_init(presenter):
    presenter.game = game
    presenter.click = click


def test_picture_10_turns(presenter):
    presenter.game.remaining_turns = 10

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '        |', '        |', '        |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_9_turns(presenter):
    presenter.game.remaining_turns = 9

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '        |', '        |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_8_turns(presenter):
    presenter.game.remaining_turns = 8

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '    |   |', '        |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_7_turns(presenter):
    presenter.game.remaining_turns = 7

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '    |   |', '    |   |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_6_turns(presenter):
    presenter.game.remaining_turns = 6

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|   |', '    |   |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_5_turns(presenter):
    presenter.game.remaining_turns = 5

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '        |', '        |', '________|_']
    assert actual == expected


def test_picture_4_turns(presenter):
    presenter.game.remaining_turns = 4

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '    |   |', '        |', '________|_']
    assert actual == expected


def test_picture_3_turns(presenter):
    presenter.game.remaining_turns = 3

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '    |   |', '   /    |', '________|_']
    assert actual == expected


def test_picture_2_turns(presenter):
    presenter.game.remaining_turns = 2

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '    |   |', '   / \  |', '________|_']
    assert actual == expected


def test_picture_1_turns(presenter):
    presenter.game.remaining_turns = 1

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '    |   |', '  _/ \  |', '________|_']
    assert actual == expected


def test_picture_0_turns(presenter):
    presenter.game.remaining_turns = 0

    actual = [line for line in presenter.picture()]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |',
                '    |   |', '  _/ \  |', '________|_']
    assert actual == expected


def test_status_0_misses(presenter):
    actual = [line for line in presenter.status()]
    expected = ['', '', '', '     MISSES:', '     _ _ _ _ _ _ _ _ _ _', '', '',
                '', '', '']

    assert actual == expected


def test_status_2_misses(presenter):
    # noinspection PySetFunctionToLiteral
    presenter.game.misses = list(set(['A', 'E']))

    actual = [line for line in presenter.status()]
    expected = ['', '', '', '     MISSES:', '     A E _ _ _ _ _ _ _ _', '', '',
                '', '', '']

    assert set(actual[4].split(' ')) == set(expected[4].split(' '))


def test_status_10_misses(presenter):
    presenter.game.misses = list(set(list('QWERTYASDF')))

    actual = [line for line in presenter.status()]
    expected = ['', '', '', '     MISSES:', '     A E D F Q S R T W Y', '', '',
                '', '', '']

    assert set(actual[4].split(' ')) == set(expected[4].split(' '))


@pytest.mark.skipif(sys.version_info > (2, 7), reason="requires python2.7")
def test_write_constructor(presenter, game, click):
    assert dir(presenter) == dir(Presenter.write(game=game, click=click))
    assert isinstance(Presenter.write(game=game, click=click).click, Mock)


@pytest.mark.skipif(sys.version_info > (2, 7), reason="requires python2.7")
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
    Presenter.write(game=game)
    out, err = capsys.readouterr()
    actual = [line.strip() for line in out.split('\n')]
    assert actual == list(map(str.strip, expected.split('\n')))
    assert err == ''


@pytest.mark.skipif(sys.version_info > (2, 7), reason="requires python2.7")
def test_flash_message(game, capsys):
    message = 'This test is a success'
    Presenter.write(game=game, flash=message)
    out, err = capsys.readouterr()
    assert out.split('\n')[0] == '{0: <45}'.format(message)
    assert err == ''


@pytest.mark.skipif(__pypy__, reason='PyPy IS statement')
def test_prompt_class_method(click):
    actual = Presenter.prompt(click)
    assert actual is 'A'


def test_play_again_prompt_class_method_true(click):
    actual = Presenter.play_again_prompt(click)
    assert actual is True


def test_play_again_prompt_class_method_false(click):
    click.confirm.return_value = False
    actual = Presenter.play_again_prompt(click)
    assert actual is False


@pytest.mark.skipif(sys.version_info > (2, 7), reason="requires python2.7")
def test_goodbye_class_method(capsys):
    Presenter.goodbye()
    out, err = capsys.readouterr()
    assert out == 'Have a nice day!\n\n'
    assert err == ''
