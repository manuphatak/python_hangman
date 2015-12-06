#!/usr/bin/env python
# coding=utf-8
import pytest

from hangman.utils import FlashMessage


@pytest.fixture
def flash():
    return FlashMessage()


def test_is_blank(flash):
    assert str(flash) is ''


def test_calling_sets_message(flash):
    flash('TEST')
    assert flash.message is 'TEST'


def test_consumption_clears_message(flash):
    flash('TEST')
    assert str(flash) is 'TEST'
    assert str(flash) is ''


def test_comparison_does_not_clear_message(flash):
    flash('TEST')
    if flash:
        pass

    assert flash
    assert flash == True  # noqa

    assert str(flash) is 'TEST'


def test_is_false_when_no_message(flash):
    assert not flash
    assert flash == False  # noqa


def test_can_be_formatted_when_empty(flash):
    assert '{0:45s}'.format(flash) == '{0:45s}'.format('')


def test_can_be_formatted_to_string(flash):
    flash('TEST')
    assert 'Hello {0}'.format(flash) == 'Hello TEST'


def test_formatting_consumes_flash_message(flash):
    flash('TEST')
    'Hello {0}'.format(flash)

    assert 'Hello {0}'.format(flash) == 'Hello '
