# coding=utf-8
from hangman import Hangman, GameOver, GameWon
from presenter import Presenter


class Commander(object):
    def __init__(self, hangman=Hangman, presenter=Presenter):
        self.game = hangman()
        self.Presenter = presenter

    @classmethod
    def run(cls, *args, **kwargs):
        flash = None
        self = cls(*args, **kwargs)
        while True:
            self.Presenter.write(self.game, flash)
            flash = None
            guess = self.Presenter.prompt()
            try:
                self.game.guess(guess)
            except GameOver:
                message = "YOU'RE AN IDIOT. THE ANSWER IS {}".format(self.game.answer)
                self.Presenter.write(self.game, message)
                break
            except GameWon:
                message = "YOU ARE SO COOL"
                self.Presenter.write(self.game, message)
                break
            except ValueError as e:
                flash = e.message
                continue

        return self


if __name__ == '__main__':
    Commander.run()
