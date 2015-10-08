# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
import io, os
from rst_cleaner import yield_sphinx_only_markup

def read_text_lines(fname):
    with io.open(os.path.join('.', fname)) as fd:
        return fd.readlines()

readme_lines = read_text_lines('README.rst')


setup(
    name = 'schematax',
    version = '0.1.4',
    author = 'Jack Fletcher',
    author_email = 'jack.mckayfletcher@plymouth.ac.uk',
    packages=find_packages(),
    url = 'https://github.com/iSTB/python-schemata',
    license = 'LICENSE.txt',
    keywords=['schemata', 'schema', 'genetic algorithms', 'GAs', 'complete lattice', 'meet', 'join'],
    description = 'A python package for all things schemata related',
    long_description = ''.join(yield_sphinx_only_markup(readme_lines)),
    install_requires=['graphviz'],
)
