# coding=utf-8
import pytest


@pytest.fixture
def mock_word_bank_get():
    from hangman.utils import WordBank

    WordBank.set('TEST')
    return WordBank.get


def test_dictionary_returns_random_choice(mock_word_bank_get):
    assert mock_word_bank_get() == 'TEST'
