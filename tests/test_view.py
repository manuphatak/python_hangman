# coding=utf-8
from textwrap import dedent

from mock import Mock
from pytest import fixture, raises

from hangman import view


@fixture(autouse=True)
def setup(monkeypatch):
    monkeypatch.setattr('click.getchar', lambda: 'A')
    monkeypatch.setattr('click.confirm', lambda _: True)


@fixture
def patch_click_output(monkeypatch):
    monkeypatch.setattr('click.secho', lambda *args, **_: None)
    monkeypatch.setattr('click.echo', lambda *args, **_: None)


@fixture
def game():
    from hangman.model import Hangman

    mock_game = Mock(spec=Hangman)
    mock_game.misses = []
    mock_game.status = '_______'
    mock_game.answer = 'HANGMAN'
    mock_game.remaining_turns = 10
    return mock_game


@fixture
def flash():
    from hangman.utils import FlashMessage

    return FlashMessage()


def test_picture_10_turns():
    remaining_turns = 10

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
                |
                |
                |
                |
                |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_picture_9_turns():
    remaining_turns = 9

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
           (_)  |
                |
                |
                |
                |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_picture_8_turns():
    remaining_turns = 8

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
           (_)  |
            |   |
                |
                |
                |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_picture_7_turns():
    remaining_turns = 7

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
           (_)  |
            |   |
            |   |
                |
                |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_picture_6_turns():
    remaining_turns = 6

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
           (_)  |
           \|   |
            |   |
                |
                |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_picture_5_turns():
    remaining_turns = 5

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
           (_)  |
           \|/  |
            |   |
                |
                |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_picture_4_turns():
    remaining_turns = 4

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
           (_)  |
           \|/  |
            |   |
            |   |
                |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_picture_3_turns():
    remaining_turns = 3

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
           (_)  |
           \|/  |
            |   |
            |   |
           /    |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_picture_2_turns():
    remaining_turns = 2

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
           (_)  |
           \|/  |
            |   |
            |   |
           / \  |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_picture_1_turns():
    remaining_turns = 1

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
           (_)  |
           \|/  |
            |   |
            |   |
          _/ \  |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_picture_0_turns():
    remaining_turns = 0

    actual = '\n'.join(view.build_partial_picture(remaining_turns))
    expected = dedent("""
            _____
            |   |
           (_)  |
           \|/  |
            |   |
            |   |
          _/ \_ |
        ________|_"""[1:])
    assert actual.splitlines() == expected.splitlines()
    assert actual == expected


def test_status_0_misses_full():
    misses = []
    actual = list(view.build_partial_misses(misses))
    expected = ['', '', '', '     MISSES:', '     _ _ _ _ _ _ _ _ _ _', '', '', '', '', '']

    assert actual == expected


def test_status_2_misses():
    misses = ['A', 'E']

    actual = list(view.build_partial_misses(misses))
    expected = ['', '', '', '     MISSES:', '     A E _ _ _ _ _ _ _ _', '', '', '', '', '']

    assert set(actual[4].split(' ')) == set(expected[4].split(' '))


def test_status_10_misses():
    misses = list('QWERTYASDF')

    actual = list(view.build_partial_misses(misses))
    expected = ['', '', '', '     MISSES:', '     A E D F Q S R T W Y', '', '', '', '', '']

    assert set(actual[4].split(' ')) == set(expected[4].split(' '))


def test_draw_board(game, capsys):
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


def test_keyboard_interrupt(monkeypatch):
    monkeypatch.setattr('click.getchar', lambda: '\x03')

    with raises(KeyboardInterrupt):
        view.prompt_guess()


def test_prompt_play_again_method_true():
    assert view.prompt_play_again() is True


def test_say_goodbye_method(capsys):
    view.say_goodbye()
    out, err = capsys.readouterr()
    assert out == 'Have a nice day!\n\n'
    assert err == ''


def test_game_won(capsys, game, flash):
    from hangman.utils import GameOverNotificationComplete

    expected = 'YOU ARE SO COOL'
    flash.game_won = True

    with raises(GameOverNotificationComplete):
        view.draw_board(game, message=flash)
    out, err = capsys.readouterr()

    assert out.startswith(expected)


def test_game_lost(capsys, game, flash):
    from hangman.utils import GameOverNotificationComplete

    expected = "YOU LOSE! THE ANSWER IS HANGMAN"
    flash.game_lost = True
    flash.game_answer = 'HANGMAN'

    with raises(GameOverNotificationComplete):
        view.draw_board(game, message=flash)
    out, err = capsys.readouterr()

    assert out.startswith(expected)
