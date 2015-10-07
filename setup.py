# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = 'schematax',
    version = '0.1.3',
    author = 'Jack Fletcher',
    author_email = 'jack.mckayfletcher@plymouth.ac.uk',
    packages=find_packages(),
    url = 'https://github.com/iSTB/python-schemata',
    license = 'LICENSE.txt',
    keywords=['schemata', 'schema', 'genetic algorithms', 'GAs', 'complete lattice', 'meet', 'join'],
    description = 'A python package for all things schemata related',
    long_description = open('README.rst').read(),
    install_requires=['graphviz'],
)
