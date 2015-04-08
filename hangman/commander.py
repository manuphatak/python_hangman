# coding=utf-8
from . import Hangman, GameOver, GameWon
from . import Presenter


class Commander(object):
    def __init__(self, hangman=Hangman, presenter=Presenter):
        self.game = hangman()
        self.Presenter = presenter

    @classmethod
    def run(cls, hangman=Hangman, presenter=Presenter):
        self = cls(hangman=hangman, presenter=presenter)
        flash = None
        play_again = False
        while True:
            self.Presenter.write(self.game, flash=flash)
            flash = None
            guess = self.Presenter.prompt()
            try:
                self.game.guess(guess)
            except GameOver:
                message = "YOU'RE AN IDIOT. THE ANSWER IS {0}".format(
                    self.game.answer)
                self.Presenter.write(self.game, flash=message, color='red')
                play_again = self.Presenter.play_again_prompt()
                break
            except GameWon:
                message = "YOU ARE SO COOL"
                self.Presenter.write(self.game, flash=message, color='cyan')
                play_again = self.Presenter.play_again_prompt()
                break
            except ValueError as e:
                flash = e.message
                continue
        if play_again:
            del self
            cls.run(hangman=hangman, presenter=presenter)
        else:
            self.Presenter.goodbye()
            return self