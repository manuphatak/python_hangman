from distutils.core import setup

setup(name='python_hangman', version='1.0.0', packages=['test', 'hangman'],
      url='https://github.com/bionikspoon/tdd_python_hangman', license='MIT',
      author='manu', author_email='bionikspoon@gmail.com',
      description='Python hangman TDD demonstration.',
      entry_points={'console_scripts': ['hangman = hangman:cli']})
