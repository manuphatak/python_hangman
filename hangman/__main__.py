# coding=utf-8
"""
hangman.__main__
~~~~~~~~~~~~~~~~

Entry point for ``hangman`` command.
"""
from __future__ import absolute_import

import click

from . import controller


@click.command()
def cli():
    controller.run()


if __name__ == '__main__':
    cli()  # pragma: no cover
