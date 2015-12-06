import os
import string
import sys
from random import choice

from mock import patch
from pycallgraph import (PyCallGraph, Config, GlobbingFilter, PyCallGraphException)
from pycallgraph.output import GraphvizOutput

from hangman import __version__ as version
from hangman.controller import game_loop


class LocalConfig:
    ITERATIONS = 100
    CHUNKS = 10
    ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def patch_getchar():
    def random_letter():
        return choice(string.ascii_uppercase)

    return random_letter


def patch_confirm():
    while True:
        for _ in list(range(LocalConfig.CHUNKS)):
            yield True
        yield False


def graphiz_setup(tool='dot'):
    graphviz = GraphvizOutput()
    graphviz.output_file = os.path.join(LocalConfig.ROOT, 'charts', 'images',
                                        'basic-{}-{}-v{}.png'.format(LocalConfig.ITERATIONS, tool, version))
    graphviz.tool = tool
    return graphviz


def config_setup():
    config = Config()
    config.trace_filter = GlobbingFilter(include=['hangman.*'])
    return config


def main(tool='dot'):
    graphviz = graphiz_setup(tool)
    config = config_setup()

    # Patch click console prompts.  Patch click printing
    with patch('click.getchar') as getchar, patch('click.confirm') as confirm, patch('click.echo'), patch(
        'click.secho'), patch('click.clear'):
        getchar.side_effect = patch_getchar()
        confirm.side_effect = patch_confirm()

        with PyCallGraph(output=graphviz, config=config):
            print('Begin: Building <%r> call chart...' % tool)
            for i in range(LocalConfig.ITERATIONS // LocalConfig.CHUNKS):
                game_loop()
                print('%4s trials completed' % ((i + 1) * LocalConfig.CHUNKS))
            print('End: Done building <%r> call chart.' % tool)


if __name__ == '__main__':
    # add project folder to PATH
    sys.path.append(LocalConfig.ROOT)

    for tool in ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']:
        try:
            main(tool)
        except PyCallGraphException as e:
            print('<%r> Failed.' % tool)
            print(e)
