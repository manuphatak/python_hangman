# coding=utf-8
import click


class Presenter():
    game = None

    def __init__(self, game=None, click=click):
        self.game = game
        self.click = click

    def picture(self):
        turns = self.game.remaining_turns
        yield '    _____'
        yield '    |   |'
        if turns <= 9:
            yield '   (_)  |'
        else:
            yield '        |'

        if turns <= 5:
            yield '   \|/  |'
        elif turns <= 6:
            yield '   \|   |'
        elif turns <= 8:
            yield '    |   |'
        else:
            yield '        |'

        if turns <= 7:
            yield '    |   |'
        else:
            yield '        |'

        if turns <= 4:
            yield '    |   |'
        else:
            yield '        |'

        if turns <= 1:
            yield '  _/ \  |'
        elif turns <= 2:
            yield '   / \  |'
        elif turns <= 3:
            yield '   /    |'
        else:
            yield '        |'

        yield '________|_'

    def status(self):
        yield ''
        yield ''
        yield ''
        yield '{:s}{:s}'.format(' ' * 5, 'MISSES:')
        misses = '{:_<10s}'.format(''.join(self.game.misses))
        yield '{:s}{:s}'.format(' ' * 5, ' '.join(list(misses)))
        yield ''
        yield ''
        yield ''
        yield ''
        yield ''

    @classmethod
    def write(cls, game=None, click=click, flash=None, color=None):
        self = cls(game=game, click=click)
        self.click.clear()

        if flash:
            color = color if color else 'yellow'
            self.click.secho('{:45s}'.format(flash), bold=True, fg=color)
        else:
            self.click.echo()

        self.click.secho('{: ^45s}'.format('HANGMAN GAME'), bold=True,
                         underline=True)

        iterate_this = zip(self.picture(), self.status(), xrange(10))
        for picture, details, i in iterate_this:
            self.click.echo('{:10s}{:35s}'.format(picture, details))

        deliminator = '   ' if len(game.status) < 45 / 4 else '  '
        status = deliminator.join(list(game.status))
        self.click.echo()
        self.click.echo('{: ^45s}'.format(status))

        return self

    @classmethod
    def prompt(cls, click=click):
        self = cls(click=click)
        self.click.echo()
        self.click.secho('Dare to pick a letter: ', dim=True, bold=True)
        return self.click.getchar(True)

    @classmethod
    def play_again_prompt(cls, click=click):
        self = cls(click=click)
        self.click.echo()
        return self.click.confirm('Double or nothings?')

    @classmethod
    def goodbye(cls, click=click):
        self = cls(click=click)
        self.click.secho('Have a nice day!', bold=True, fg='green', blink=True)
