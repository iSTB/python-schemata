# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
import io, os
from rst_cleaner import yield_sphinx_only_markup
#from Cython.Build import cythonize
from distutils.extension import Extension
try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass = { }
ext_modules = [ ]

if use_cython:
    ext_modules += [
        Extension("schematax.schemata", [ "schematax/schemata.pyx" ]),
    ]
    cmdclass.update({ 'build_ext': build_ext })
else:
    ext_modules += [
        Extension("schematax.schemata", [ "schematax/schemata.pyx" ]),
    ]



def read_text_lines(fname):
    with io.open(os.path.join('.', fname)) as fd:
        return fd.readlines()

readme_lines = read_text_lines('README.rst')


setup(
    name = 'schematax',
    version = '0.1.7',
    author = 'Jack Fletcher',
    cmdclass = cmdclass,
    ext_modules=ext_modules,
    author_email = 'jack.mckayfletcher@plymouth.ac.uk',
    packages=find_packages(),
    url = 'https://github.com/iSTB/python-schemata',
    license = 'LICENSE.txt',
    keywords=['schemata', 'schema', 'genetic algorithms', 'GAs', 'complete lattice', 'meet', 'join'],
    description = 'A python package for all things schemata related',
    long_description = ''.join(yield_sphinx_only_markup(readme_lines)),
    install_requires=['graphviz','numpy'],
)
