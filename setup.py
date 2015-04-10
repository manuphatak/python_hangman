import sys
import re

from setuptools import setup
from setuptools.command.test import test as TestCommand


version_re = re.compile(r"(?<=^__version__ = \')[\w\.]+(?=\'$)", re.U | re.M)
with open('hangman/__init__.py', 'rb') as f:
    version = version_re.search(f.read().decode('utf-8')).group()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)

# @f:off
setup(name='python_hangman',
      version=version,
      packages=['hangman'],
      url='https://github.com/bionikspoon/Hangman',
      license='MIT',
      author='Manu',
      author_email='bionikspoon@gmail.com',
      description='Python hangman TDD demonstration.',
      keywords='python tdd hangman',
      install_requires=['click',
                        'future'],
      use_2to3=True,
      tests_require=['tox',
                     'pytest',
                     'mock'],
      cmdclass={'test': PyTest},
      entry_points={'console_scripts': ['hangman = hangman:cli']},
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: Implementation :: '
                   'CPython',
                   'Programming Language :: Python :: Implementation :: PyPy',
                   'Topic :: Games/Entertainment :: Puzzle Games',
                   'Topic :: Terminals'])

# @f:on