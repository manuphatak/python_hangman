from mock import patch
from pycallgraph import PyCallGraph, Config, GlobbingFilter
from pycallgraph.output import GraphvizOutput

from hangman import Commander


def main(tool='dot'):
    graphviz = GraphvizOutput()
    graphviz.output_file = 'charts/basic-{}.png'.format(tool)
    graphviz.tool = tool

    config = Config()
    config.trace_filter = GlobbingFilter(include=['hangman.*'])
    with patch('click.getchar') as getchar_, patch('click.confirm') as confirm_:
        getchar_.side_effect = list('QWERTYUIOPASDFGHJKLZXCVBNM' * 2)
        confirm_.side_effect = [True, False]
        with PyCallGraph(output=graphviz, config=config):
            Commander.run()


if __name__ == '__main__':
    main('dot')
    main('neato')
    main('fdp')
    # main('sfdp')
    main('twopi')
    main('circo')
