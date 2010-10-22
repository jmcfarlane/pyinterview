=====================
Software version sort
=====================

Goal
++++

A common versioning scheme is major.minor.version, for example:
``1.2.3``.  Create a function that properly sorts version numbers that
match this pattern.

Definition
++++++++++

The tricky part about software version numbers is that a simple ascii
sort isn't always accurate.  Take the following example::

 >>> versions = ['1.10.3', '1.2.2', '1.11.1']
 >>> versions.sort(reverse=True)
 >>> for version in versions:
 ...     print version
 ...
 1.2.2
 1.11.1 # Note this one is actually the highest version!
 1.10.3

The sort is incorrect because ``"2"`` sorts before ``"11"`` on a
descending sort.

REFERENCE: http://en.wikipedia.org/wiki/Software_versioning

Requirements
++++++++++++

The function should have the following signature::

 def sort_versions(versions):
    pass

The function should be called with the following data::

 >>> sort_versions(['1.10.3', '1.2.2', '1.11.1'])

And should do a proper sort on the version strings, in descending
order - meaning the highest version numbers print first.

Output
^^^^^^

The function should print to stdout, in the form of one version string
per line.

Correct answer
++++++++++++++

This is the expected correct answer::
 
 >>> sort_versions(['1.10.3', '1.2.2', '1.11.1'])
 1.11.1
 1.10.3
 1.2.2
