# coding=utf-8
from textwrap import dedent

import pytest
from mock import Mock

from hangman import view
from hangman.utils import GameFinished

try:
    import __pypy__
except ImportError:
    __pypy__ = None


@pytest.fixture
def game():
    from hangman.hangman import Hangman

    mock_game = Mock(spec=Hangman)
    mock_game.return_value = mock_game
    mock_game.misses = []
    mock_game.status = '_______'
    mock_game.answer = 'HANGMAN'
    mock_game.remaining_turns = 10
    return mock_game


@pytest.fixture(autouse=True)
def setup(monkeypatch):
    import codecs

    def is_ascii_encoding(encoding):
        """Checks if a given encoding is ascii."""
        try:
            return codecs.lookup(encoding).name == 'ascii'
        except (LookupError, TypeError):
            return False

    monkeypatch.setattr('click.getchar', lambda: 'A')
    monkeypatch.setattr('click.confirm', lambda _: True)
    monkeypatch.setattr('click._compat.is_ascii_encoding', is_ascii_encoding)


@pytest.fixture
def flash():
    from hangman.utils import FlashMessage

    return FlashMessage()


def test_picture_10_turns():
    remaining_turns = 10

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '        |', '        |', '        |', '        |', '        |', '________|_']
    assert actual == expected


def test_picture_9_turns():
    remaining_turns = 9

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '   (_)  |', '        |', '        |', '        |', '        |', '________|_']
    assert actual == expected


def test_picture_8_turns():
    remaining_turns = 8

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '   (_)  |', '    |   |', '        |', '        |', '        |', '________|_']
    assert actual == expected


def test_picture_7_turns():
    remaining_turns = 7

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '   (_)  |', '    |   |', '    |   |', '        |', '        |', '________|_']
    assert actual == expected


def test_picture_6_turns():
    remaining_turns = 6

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|   |', '    |   |', '        |', '        |', '________|_']
    assert actual == expected


def test_picture_5_turns():
    remaining_turns = 5

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |', '        |', '        |', '________|_']
    assert actual == expected


def test_picture_4_turns():
    remaining_turns = 4

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |', '    |   |', '        |', '________|_']
    assert actual == expected


def test_picture_3_turns():
    remaining_turns = 3

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |', '    |   |', '   /    |', '________|_']
    assert actual == expected


def test_picture_2_turns():
    remaining_turns = 2

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |', '    |   |', '   / \  |', '________|_']
    assert actual == expected


def test_picture_1_turns():
    remaining_turns = 1

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |', '    |   |', '  _/ \  |', '________|_']
    assert actual == expected


def test_picture_0_turns():
    remaining_turns = 0

    actual = [line for line in view.partial_picture(remaining_turns)]
    expected = ['    _____', '    |   |', '   (_)  |', '   \|/  |', '    |   |', '    |   |', '  _/ \  |', '________|_']
    assert actual == expected


def test_status_0_misses_full():
    misses = []
    actual = list(view.partial_status(misses))
    expected = ['', '', '', '     MISSES:', '     _ _ _ _ _ _ _ _ _ _', '', '', '', '', '']

    assert actual == expected


def test_status_2_misses():
    misses = ['A', 'E']

    actual = [line for line in view.partial_status(misses)]
    expected = ['', '', '', '     MISSES:', '     A E _ _ _ _ _ _ _ _', '', '', '', '', '']

    assert set(actual[4].split(' ')) == set(expected[4].split(' '))


def test_status_10_misses():
    misses = list('QWERTYASDF')

    actual = [line for line in view.partial_status(misses)]
    expected = ['', '', '', '     MISSES:', '     A E D F Q S R T W Y', '', '', '', '', '']

    assert set(actual[4].split(' ')) == set(expected[4].split(' '))


def test_write_output(game, capsys):
    expected_list = dedent("""
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
""").split('\n')
    view.draw_board(game)
    out, err = capsys.readouterr()
    actual_list = out.split('\n')
    for actual_list, expected in zip(actual_list, expected_list):
        assert actual_list.rstrip() == expected.rstrip()
    assert err == ''


def test_flash_message(game, capsys, flash):
    message = 'This test is a success'
    flash(message)
    view.draw_board(game, message=flash)
    out, err = capsys.readouterr()
    assert out.split('\n')[0] == '{0: <45}'.format(message)
    assert err == ''


def test_flash_message_handles_error_objects(game, capsys, flash):
    message = 'This test is a success'

    try:
        raise ValueError(message)
    except ValueError as e:
        flash(e)
        view.draw_board(game, message=flash)

    out, err = capsys.readouterr()
    assert out.split('\n')[0] == '{0: <45}'.format(message)
    assert err == ''


def test_prompting_for_a_guess():
    actual = view.prompt_guess()
    assert actual == 'A'


def test_prompt_play_again_method_true():
    assert view.prompt_play_again() is True


def test_say_goodbye_method(capsys):
    view.say_goodbye()
    out, err = capsys.readouterr()
    assert out == 'Have a nice day!\n\n'
    assert err == ''


def test_game_won(capsys, game, flash):
    expected = 'YOU ARE SO COOL'
    flash.game_won = True

    with pytest.raises(GameFinished):
        view.draw_board(game, message=flash)
    out, err = capsys.readouterr()

    assert out.startswith(expected)


def test_game_over(capsys, game, flash):
    expected = "CAN'T EVEN WIN HANGMAN? THE ANSWER IS HANGMAN"
    flash.game_over = True
    flash.game_answer = 'HANGMAN'

    with pytest.raises(GameFinished):
        view.draw_board(game, message=flash)
    out, err = capsys.readouterr()

    assert out.startswith(expected)
