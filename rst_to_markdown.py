# #!/usr/bin/env python
# # coding=utf-8
# import os
# import re
# from functools import partial
#
# import pypandoc
# import click
# from os.path import isfile, join, abspath, normpath
#
# INCLUDE = '.. include:: '
#
# re_include = re.compile('^(?:\.\. include:: )(\S+)$')
#
#
# class Config:
#     src = os.getcwd()
#     path = partial(join, src)
#
#
# def include_directive(line):
#     if not line.startswith(INCLUDE):
#         return line
#
#     include_file = line.replace(INCLUDE, '')
#     if not isfile(normpath(Config.path(include_file))):
#         print(normpath(Config.path(include_file)))
#         raise Exception
#
#
# def get_file_text(src):
#     with open(src) as src_file:
#         file_text = [include_directive(line) for line in src_file]
#     return file_text
#
#
# @click.command()
# @click.argument('src', type=click.Path(exists=True, dir_okay=False))
# def convert(src):
#     print(abspath(src))
#     Config.src = abspath(src)
#     file_text = get_file_text(Config.src)
#
#     print(file_text)
#
#
# if __name__ == '__main__':
#     convert()
