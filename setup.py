# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name = 'schematax',
    version = '0.1',
    author = 'Jack Fletcher',
    author_email = 'jack.mckayfletcher@plymouth.ac.uk',
    packages = ['schematax'],
    url = 'https://github.com/iSTB/python-schemata',
    license = 'LICENSE',
    keywords=['schemata', 'schema', 'genetic algorithms', 'GAs', 'complete lattice', 'meet', 'join'],
    description = 'A python package for all things schemata related',
    long_description = open('README.rst').read(),
    install_requires=['graphviz'],
)
