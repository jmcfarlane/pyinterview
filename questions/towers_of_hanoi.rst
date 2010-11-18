===============
Towers of Hanoi
===============

Goal
++++

Create a function to solve the Towers of Hanoi puzzle.

Definition
++++++++++

The Tower of Hanoi or Towers of Hanoi is a mathematical game or
puzzle. It consists of three rods, and a number of disks of different
sizes which can slide onto any rod. The puzzle starts with the disks
in a neat stack in ascending order of size on one rod, the smallest at
the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another
rod, obeying the following rules:

* Only one disk may be moved at a time.
* Each move consists of taking the upper disk from one of the rods and
  sliding it onto another rod, on top of the other disks that may
  already be present on that rod.
* No disk may be placed on top of a smaller disk.

REFERENCE: http://en.wikipedia.org/wiki/Tower_of_Hanoi

Requirements
++++++++++++

The function should have the following signature::

 def towers(disc, src, aux, dest):
    pass

The above function will be called like this::

 >>> towers(3, 'Source', 'Auxillary', 'Destination')

Output
^^^^^^

The function should print to stdout the correct disc moves in the
proper order, one move per line.  The format of each line should be
something like::

 Move disc 2 from Auxillary to Destination

Correct answer
++++++++++++++

This is the expected correct answer::
 
 Move disc 1 from Source to Destination
 Move disc 2 from Source to Auxillary
 Move disc 1 from Destination to Auxillary
 Move disc 3 from Source to Destination
 Move disc 1 from Auxillary to Source
 Move disc 2 from Auxillary to Destination
 Move disc 1 from Source to Destination
