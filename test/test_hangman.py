# coding=utf-8
import pytest
from hangman.hangman import Hangman


@pytest.fixture
def game():
    return Hangman('hangman')


def test_new_game_returns_game_instance_with_answer(game):
    assert game.answer == 'HANGMAN'


def test_new_game_returns_game_instance_with_misses(game):
    assert game.misses == []


def test_new_game_returns_game_instance_with_remaining_turns(game):
    assert game.remaining_turns == 10


def test_new_game_returns_game_instance_with_status(game):
    assert game.status == '_______'


def test_guess_miss_removes_1_turn(game):
    game.guess('e')
    assert game.remaining_turns == 9


def test_guess_miss_updates_misses(game):
    game.guess('e')
    assert game.misses == ['E']



