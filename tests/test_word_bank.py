# coding=utf-8
from functools import partial

import pytest


@pytest.fixture
def mock_get_random():
    from hangman.word_bank import get_random

    WORDS = ['TEST']
    return partial(get_random, choices=WORDS)


def test_dictionary_returns_random_choice(mock_get_random):
    assert mock_get_random() == 'TEST'
