#!/usr/bin/env python
# coding=utf-8

"""
test_hangman
----------------------------------

Tests for `Hangman` model.
"""
import pytest
from hangman.model import Hangman, GameWon, GameOver


@pytest.fixture
def game():
    return Hangman(answer='hangman')


def test_new_game_returns_game_instance_with_answer(game):
    assert game.answer == 'HANGMAN'


def test_new_game_returns_game_instance_with_misses(game):
    assert game.misses == []


def test_new_game_returns_game_instance_with_remaining_turns(game):
    assert game.remaining_turns == 10


def test_new_game_returns_game_instance_with_status(game):
    assert game.status == '_______'


def test_answer_validation_rules():
    with pytest.raises(ValueError):
        Hangman('1234567')

    with pytest.raises(ValueError):
        Hangman('hangman12')

    with pytest.raises(ValueError):
        Hangman(1232145678995462313)

    with pytest.raises(ValueError):
        Hangman('a' * 100)
    with pytest.raises(ValueError):
        Hangman('a' * 17)

    with pytest.raises(ValueError):
        Hangman('hand-work')


def test_guess_miss_removes_1_turn(game):
    game.guess('e')
    assert game.remaining_turns == 9


def test_guess_miss_updates_misses(game):
    game.guess('e')
    assert game.misses == ['E']


def test_guess_miss_does_not_change_status(game):
    expected = game.status
    game.guess('e')
    assert game.status == expected == '_______'


def test_guess_validation_must_be_a_single_letter_number(game):
    with pytest.raises(ValueError):
        game.guess(1)

    with pytest.raises(ValueError):
        game.guess('EE')

    with pytest.raises(ValueError):
        game.guess('')


def test_guess_miss_duplicate_is_ignored(game):
    game.guess('e')
    game.guess('e')
    assert game.remaining_turns == 9


def test_guess_hit_updates_status(game):
    game.guess('a')
    assert game.status == '_A___A_'

    game.guess('H')
    assert game.status == 'HA___A_'


def test_guess_hit_leaves_remaining_turns_and_misses_untouched(game):
    expected_misses = game.misses
    expected_remaining_turns = game.remaining_turns

    game.guess('a')

    assert expected_misses == game.misses
    assert expected_remaining_turns == game.remaining_turns


def test_game_winning_guess(game):
    game.guess('h')
    game.guess('a')
    game.guess('n')
    game.guess('g')

    with pytest.raises(GameWon):
        game.guess('m')

    assert game.status == 'HANGMAN'


def test_setting_hits_can_raise_game_won(game):
    with pytest.raises(GameWon):
        game.hits = list('HANGMAN')


def test_game_losing_guess(game):
    game.guess('b')
    game.guess('c')
    game.guess('d')
    game.guess('e')
    game.guess('f')
    game.guess('i')
    game.guess('j')
    game.guess('k')
    game.guess('l')

    with pytest.raises(GameOver):
        game.guess('o')
    assert game.status == '_______'
    assert game.remaining_turns == 0


def test_setting_misses_can_raise_game_over(game):
    with pytest.raises(GameOver):
        game.misses = list('BCDEFIJKLO')


def test_game_populates_answer_if_not_provided():
    from hangman.utils import WordBank

    WordBank.set('TEST')

    _game = Hangman()
    assert _game.answer == 'TEST'


def test_game_repr(game):
    expected = "hangman(status='_______', misses=[], remaining_turns=10)"
    assert repr(game) == expected
