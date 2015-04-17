#!/usr/bin/env python
# coding=utf-8
"""
Documentation
-------------

The full documentation is at https://python-hangman.readthedocs.org.
"""
import os
import sys
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools.command.test import test as TestCommand

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)


_version_re = re.compile(r"(?<=^__version__ = \')[\w\.]+(?=\'$)", re.U | re.M)
with open('hangman/__init__.py', 'rb') as f:
    version = _version_re.search(f.read().decode('utf-8')).group()

with open('README.rst') as f:
    readme = f.read()

with open('HISTORY.rst') as f:
    history = f.read().replace('.. :changelog:', '')

# @:on
setup(name='python_hangman',
      version=version,
      description='Python hangman TDD demonstration.',
      long_description=readme + '\n\n' + __doc__ + '\n\n' + history,
      author='Manu Phatak',
      author_email='bionikspoon@gmail.com',
      url='https://github.com/bionikspoon/Hangman',
      keywords='python tdd hangman',
      packages=['hangman'],
      package_dir={'python_hangman': 'python_hangman'},
      include_package_data=True,
      install_requires=['click', 'future'],
      license='MIT',
      zip_safe=False,
      use_2to3=True,
      cmdclass={'test': PyTest},
      tests_require=['pytest', 'mock'],
      entry_points={'console_scripts': ['hangman = hangman.__main__:cli']},
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

# @:off
