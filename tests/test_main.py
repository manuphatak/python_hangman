#!/usr/bin/env python
# coding=utf-8
from mock import Mock
from pytest import fixture


@fixture(autouse=True)
def setup(monkeypatch, game_loop):
    monkeypatch.setattr('hangman.controller.game_loop', game_loop)


@fixture
def game_loop():
    return Mock()


@fixture
def runner():
    from click.testing import CliRunner

    return CliRunner()


def test_click_starts_game_loop(game_loop, runner):
    from hangman.__main__ import cli

    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert game_loop.call_count == 1
