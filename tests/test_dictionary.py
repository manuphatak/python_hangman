# coding=utf-8
import pytest
from hangman import Dictionary


@pytest.fixture
def MockDictionary():
    Dictionary.WORDS = ['TEST']
    return Dictionary


def test_dictionary_returns_random_choice(MockDictionary):
    assert MockDictionary()() == 'TEST'