# -*- coding:utf-8 -*-
from distutils.core import setup

setup(
    name = 'schemata',
    version = '0.0.1',
    author = 'Jack Fletcher',
    author_email = 'jack.mckayfletcher@plymouth.ac.uk',
    packages = ['schemata'],
    url = 'https://github.com/iSTB/python-schemata',
    license = 'LICENSE.txt',
    description = 'Python library for all things schemata related',
    long_description = open('README').read(),
    install_requires=['itertools'],
)
