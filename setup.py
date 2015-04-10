import sys
import re

from setuptools import setup
from setuptools.command.test import test as test_command

version_re = re.compile(r"(?<=^__version__ = \')[\w\.]+(?=\'$)", re.U | re.M)
with open('hangman/__init__.py', 'rb') as f:
    version = version_re.search(f.read().decode('utf-8')).group()

# noinspection PyAttributeOutsideInit
class Tox(test_command):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex

        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)

# @f:off
setup(name='python_hangman',
      version=version,
      packages=['hangman'],
      url='https://github.com/bionikspoon/tdd_python_hangman',
      license='MIT',
      author='manu',
      author_email='bionikspoon@gmail.com',
      description='Python hangman TDD demonstration.',
      keywords='python tdd hangman',
      install_requires=['click',
                        'future'],
      use_2to3=True,
      tests_require=['tox',
                     'pytest',
                     'mock'],
      cmdclass={'test': Tox},
      entry_points={'console_scripts': ['hangman = hangman:cli']})
# @f:on