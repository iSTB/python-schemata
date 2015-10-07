# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name = 'schemata',
    version = '0.0.1',
    author = 'Jack Fletcher',
    author_email = 'jack.mckayfletcher@plymouth.ac.uk',
    packages = ['schemata'],
    url = 'https://github.com/iSTB/python-schemata',
    license = 'LICENSE.txt',
    keywords=['schemata', 'schema', 'genetic algorithms', 'GAs', 'complete lattice', 'meet', 'join'],
    description = 'Python library for all things schemata related',
    long_description = open('README.rst').read(),
    install_requires=['graphviz'],
)
