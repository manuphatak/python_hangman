#!/usr/bin/env python
# coding=utf-8
import pytest
from mock import Mock


@pytest.fixture(autouse=True)
def setup(monkeypatch, game_loop):
    monkeypatch.setattr('hangman.controller.game_loop', game_loop)


@pytest.fixture
def game_loop():
    return Mock()


@pytest.fixture
def runner():
    from click.testing import CliRunner

    return CliRunner()


def test_click_starts_game_loop(game_loop, runner):
    from hangman.__main__ import cli

    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert game_loop.call_count == 1
