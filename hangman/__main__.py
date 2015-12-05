# coding=utf-8
"""
Entry point for ``hangman`` command.
"""
from __future__ import absolute_import
import click

from .controller import game_loop


@click.command()
def cli():
    """
    Start a new game.
    """
    game_loop()


if __name__ == '__main__':
    cli()
