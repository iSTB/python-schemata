Schemata
========

|PyPI version| |License| |Supported Python| |Format| |Downloads|

Schemata is a simple Python package to do all things related to schemata_.

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
- PyPI: http://pypi.python.org/pypi/concepts
- Documentation: http://concepts.readthedocs.org
- Changelog: http://concepts.readthedocs.org/en/latest/changelog.html
- Issue Tracker: https://github.com/iSTB/python-schemata/issues
- Download: http://pypi.python.org/pypi/concepts#downloads


Installation
------------

This package runs under Python 2.7 and 3.3+, use pip_ to install:

.. code:: bash

    $ pip install schemata

This will also install the graphviz_ package from PyPI as
required dependencies.

Rendering lattice graphs depends on the `Graphviz software`_. Make sure its
``dot`` executable is on your systems' path.


Quickstart
----------
The file example.py gives a good overview of how to use the package.

Basic schema operations:

.. code-block:: python

    >>> import schemata

    >>> s = schemata.schema('10*1') #makes a schema

    >>> s
    10*1

    >>> s.get_order()
    3

    >>> s.get_defining_length()
    3

    >>> s2 = schemata.schema('1**1') #makes another schema

    >>> s <= s2 
    True

    >>> s < s2
    True

    >>> s == s2
    False
 
    >>> schemata.meet(s,s2)
    10*1

    >>> schemata.join(s,s2)
    1**1

    >>> s3 = schemata.schema('00*1')
    
    >>> schemata.supremum([s,s2,s3])
    ***1

    >>> schemata.infimum([s,s2,s3])
    e                               #e stands for the empty schema

Schematic completion and drawing the schematic lattice:

.. code-block:: python
    
    >>> import schemata
    
    >>> xs = ['111', '011', '001']
    
    >>> ss = schemata.complete(xs) #performing schematic completion 
    
    >>> ss
    [111, 011, 001, *11, **1, 0*1, e] #e stands for the empty schema

    >>> schemata.draw(ss,'my_lattice') #draws the schematic lattice of ss and saves it as my_lattice.pdf 
    

The image produced here:

.. image:: https://raw.github.com/iSTB/python-schemata/blob/master/docs/my_lattice.pdf
    :align: center
.. image:: https://raw.github.com/xflr6/concepts/master/docs/holy-grail.png
    :align: center


Further reading
---------------

- http://en.wikipedia.org/wiki/Formal_concept_analysis
- http://www.upriss.org.uk/fca/

The generation of the concept lattice is based on the algorithm from C. Lindig.
`Fast Concept Analysis`_. In Gerhard Stumme, editors, Working with Conceptual
Structures - Contributions to ICCS 2000, Shaker Verlag, Aachen, Germany, 2000.

The included example ``CXT`` files are taken from Uta Priss' `FCA homepage`_


See also
--------

The implementation is based on these Python packages:

- bitsets_ |--| Ordered subsets over a predefined domain
- graphviz_ |--| Simple Python interface for Graphviz

The following package is build on top of concepts:

- features_ |--| Feature set algebra for linguistics

If you want to apply FCA to bigger data sets, you might want to consider `other
implementations`_ based on `more sophisticated algorithms`_ like In-Close_
or Fcbo_.


License
-------

Concepts is distributed under the `MIT license`_.



.. _Complete Lattice: https://en.wikipedia.org/wiki/Complete_lattice
.. _schemata: https://en.wikipedia.org/wiki/Schema_%28genetic_algorithms%29
.. _FCA: http://en.wikipedia.org/wiki/Formal_concept_analysis
.. _Fast Concept Analysis: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.143.948
.. _FCA homepage: http://www.upriss.org.uk/fca/examples.html

.. _pip: http://pip.readthedocs.org
.. _Graphviz software: http://www.graphviz.org


.. _bitsets: http://pypi.python.org/pypi/bitsets
.. _graphviz: http://pypi.python.org/pypi/graphviz
.. _features: http://pypi.python.org/pypi/features

.. _other implementations: http://www.upriss.org.uk/fca/fcasoftware.html
.. _more sophisticated algorithms: http://www.upriss.org.uk/fca/fcaalgorithms.html
.. _In-Close: http://sourceforge.net/projects/inclose/
.. _Fcbo: http://fcalgs.sourceforge.net

.. _MIT license: http://opensource.org/licenses/MIT


.. |--| unicode:: U+2013


.. |PyPI version| image:: https://img.shields.io/pypi/v/concepts.svg
    :target: https://pypi.python.org/pypi/concepts
    :alt: Latest PyPI Version
.. |License| image:: https://img.shields.io/pypi/l/concepts.svg
    :target: https://pypi.python.org/pypi/concepts
    :alt: License
.. |Supported Python| image:: https://img.shields.io/pypi/pyversions/concepts.svg
    :target: https://pypi.python.org/pypi/concepts
    :alt: Supported Python Versions
.. |Format| image:: https://img.shields.io/pypi/format/concepts.svg
    :target: https://pypi.python.org/pypi/concepts
    :alt: Format
.. |Downloads| image:: https://img.shields.io/pypi/dm/concepts.svg
    :target: https://pypi.python.org/pypi/concepts
    :alt: Downloads

