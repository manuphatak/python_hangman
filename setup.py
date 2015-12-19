#!/usr/bin/env python
# coding=utf-8
"""
The full documentation is at https://python_hangman.readthedocs.org.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        import sys

        errno = pytest.main(self.test_args)
        sys.exit(errno)


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['click', 'future']

test_requirements = ['pytest', 'mock']

setup(  # :off
    name='python_hangman',
    version='2.2.1',
    description='Python Hangman TDD/MVC demonstration.',
    long_description='\n\n'.join([readme, history]),
    author='Manu Phatak',
    author_email='bionikspoon@gmail.com',
    url='https://github.com/bionikspoon/python_hangman',
    packages=['hangman',],
    package_dir={'hangman':'hangman'},
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    use_2to3=True,
    cmdclass={'test': PyTest},
    keywords='python_hangman Manu Phatak',
    entry_points={'console_scripts': ['hangman = hangman.__main__:cli']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Terminals',
    ],
    test_suite='tests',
    tests_require=test_requirements
)  # :on
