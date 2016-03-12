schematax
=========

|PyPI version| |License| |Supported Python| |Format| |Downloads|

schematax is a simple Python package to do all things related to schemata_.

A schema is word made using an extra symbol, '*', called the wild card symbol.
For example the schema over the binary aplhapbet '1*0', represents the set of
strings. {'100','110'}'.

Schema have properties. For example, for a schema s, the order of s is the
number of symbols in s which are not the wild card symbols (called fixed symbols).
The defining length of s is the distance between the first and last fixed symbol.  

Given a set of words of the same length S, the schematic completion of S
returns all schema which make subsets of the words in S. 
Whats more given the partial ordering over schemata, the schematic completion of S
forms a `Complete Lattice`_.      


Links
-----

- GitHub:https://github.com/iSTB/python-schemata
- PyPI: http://pypi.python.org/pypi/schematax
- Issue Tracker: https://github.com/iSTB/python-schemata/issues
- Download: http://pypi.python.org/pypi/schematax#downloads


Installation
------------

This package runs under Python 2.7, use pip_ to install:

.. code:: bash

    $ pip install schematax

This will also install the graphviz_ package from PyPI as
required dependencies.

Or

Download the package from here, go to the python-schema directory and run:

.. code:: bash
    $ python setup.py install 

**Important**: Drawing the the schematic lattice uses `Graphviz software`_. Make sure it
is installed and ``dot`` executable is on your systems' path.


Quickstart
----------
The file example.py gives a good overview of how to use the package.

Basic schema operations:

.. code-block:: python

    >>> import schematax

    >>> s = schematax.schema('10*1') #makes a schema

    >>> s
    10*1

    >>> s.get_order()
    3

    >>> s.get_defining_length()
    3

    >>> s2 = schematax.schema('1**1') #makes another schema

    >>> s <= s2 
    True

    >>> s < s2
    True

    >>> s == s2
    False
 
    >>> schematax.meet(s,s2)
    10*1

    >>> schematax.join(s,s2)
    1**1

    >>> s3 = schematax.schema('00*1')
    
    >>> schematax.supremum([s,s2,s3])
    ***1

    >>> schematax.infimum([s,s2,s3])
    e                               #e stands for the empty schema

Schematic completion and drawing the schematic lattice:

.. code-block:: python
    
    >>> import schematax
    
    >>> xs = ['111', '011', '001']
    
    >>> ss = schematax.complete(xs) #performing schematic completion 
    
    >>> ss
    [111, 011, 001,``*11``, ``**1``, ``0*1``, e] #e stands for the empty schema

    >>> schematax.draw(ss,'my_lattice') #draws the schematic lattice of ss and saves it as my_lattice.pdf 
    

The image produced here:

.. image:: https://github.com/iSTB/python-schemata/blob/master/docs/my_lattice.png?raw=true
    :align: center


Further reading
---------------

- https://en.wikipedia.org/wiki/Schema_%28genetic_algorithms%29
- https://en.wikipedia.org/wiki/Lattice_%28order%29

See also
--------

The implementation is based on these Python packages:

- graphviz_ |--| Simple Python interface for Graphviz





License
-------

Schemata is distributed under the `MIT license`_.



.. _Complete Lattice: https://en.wikipedia.org/wiki/Complete_lattice
.. _schemata: https://en.wikipedia.org/wiki/Schema_%28genetic_algorithms%29

.. _pip: http://pip.readthedocs.org
.. _Graphviz software: http://www.graphviz.org


.. _graphviz: http://pypi.python.org/pypi/graphviz


.. _MIT license: http://opensource.org/licenses/MIT


.. |--| unicode:: U+2013


.. |PyPI version| image:: https://img.shields.io/pypi/v/schematax.svg
    :target: https://pypi.python.org/pypi/schematax
    :alt: Latest PyPI Version
.. |License| image:: https://img.shields.io/pypi/l/schematax.svg
    :target: https://pypi.python.org/pypi/concepts
    :alt: License
.. |Supported Python| image:: https://img.shields.io/pypi/pyversions/schematax.svg
    :target: https://pypi.python.org/pypi/schematax
    :alt: Supported Python Versions
.. |Format| image:: https://img.shields.io/pypi/format/schematax.svg
    :target: https://pypi.python.org/pypi/concepts
    :alt: Format
.. |Downloads| image:: https://img.shields.io/pypi/dm/schematax.svg
    :target: https://pypi.python.org/pypi/schematax
    :alt: Downloads

