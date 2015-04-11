from contextlib import contextmanager
import string
from random import choice
from cStringIO import StringIO
import sys

from mock import patch
from pycallgraph import (PyCallGraph, Config, GlobbingFilter,
                         PyCallGraphException)
from pycallgraph.output import GraphvizOutput

from hangman import Commander


ITERATIONS = 100
CHUNKS = 10


@contextmanager
def capture():
    old_out, old_err = sys.stdout, sys.stderr
    print "In..."
    try:
        out, err = StringIO(), StringIO()
        sys.stdout, sys.stderr = out, err
        yield (out, err)
    finally:
        sys.stdout, sys.stderr = old_out, old_err
        out, err = out.getvalue(), err.getvalue()
        print "Out..."


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
            for i in xrange(ITERATIONS):
                Commander.run()


if __name__ == '__main__':
    try:
        main('dot')
    except PyCallGraphException:
        pass

    # try:
    #     main('neato')
    # except PyCallGraphException:
    #     pass
    #
    # try:
    #     main('fdp')
    # except PyCallGraphException:
    #     pass
    #
    # try:
    #     main('sfdp')
    # except PyCallGraphException:
    #     pass
    #
    # try:
    #     main('twopi')
    # except PyCallGraphException:
    #     pass
    #
    # try:
    #     main('circo')
    # except PyCallGraphException:
    #     pass
