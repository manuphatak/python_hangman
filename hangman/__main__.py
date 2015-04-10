# coding=utf-8
import click

from . import Commander


@click.command()
def cli():
    Commander.run()


if __name__ == '__main__':
    cli()