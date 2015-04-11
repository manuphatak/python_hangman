# coding=utf-8
"""
    hangman.__main__ module
    =======================

    Entry point for `hangman` command.
"""
import click

from . import Commander


@click.command()
def cli():
    """
    Start a new game.
    """
    Commander.run()


if __name__ == '__main__':
    cli()