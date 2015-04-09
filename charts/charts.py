import string
from random import choice

from mock import patch
from pycallgraph import PyCallGraph, Config, GlobbingFilter
from pycallgraph.output import GraphvizOutput

from hangman import Commander


ITERATIONS = 10
CHUNKS = 100


def random_letter():
    return choice(string.ascii_uppercase)


def new_game():
    while True:
        for _ in xrange(CHUNKS):
            yield True
        yield False


def main(tool='dot'):
    graphviz = GraphvizOutput()
    graphviz.output_file = 'charts/basic-{}-{}.png'.format(ITERATIONS * CHUNKS,
                                                           tool)
    graphviz.tool = tool

    config = Config()
    config.trace_filter = GlobbingFilter(include=['hangman.*'])
    with patch('click.getchar') as getchar_, patch('click.confirm') as confirm_:
        getchar_.side_effect = random_letter
        confirm_.side_effect = new_game()
        with PyCallGraph(output=graphviz, config=config):
            for _ in xrange(ITERATIONS):
                Commander.run()


if __name__ == '__main__':
    main('dot')
    main('neato')
    # main('fdp')
    # # main('sfdp')
    # main('twopi')
    # main('circo')
