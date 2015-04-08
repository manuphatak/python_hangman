from distutils.core import setup
from setuptools.command.test import test as TestCommand
import sys


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex

        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)


setup(name='python_hangman',
      version='1.0.1',
      packages=['hangman'],
      url='https://github.com/bionikspoon/tdd_python_hangman',
      license='MIT',
      author='manu',
      author_email='bionikspoon@gmail.com',
      description='Python hangman TDD demonstration.',
      keywords='python tdd hangman',
      install_requires=['click', 'future'],
      tests_require=['pytest',
                     'mock',
                     'tox'],
      cmdclass={'test': Tox},
      entry_points={'console_scripts': ['hangman = hangman:cli']})
