# coding=utf-8
import pytest

from hangman import Dictionary


@pytest.fixture
def mock_dictionary():
    Dictionary.WORDS = ['TEST']
    return Dictionary


def test_dictionary_returns_random_choice(mock_dictionary):
    assert mock_dictionary()() == 'TEST'