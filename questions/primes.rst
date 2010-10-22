=======================
Prime number generation
=======================

Goal
++++

The primary goal of this question is to create a function that
correctly calculates prime numbers.  A secondary goal is the speed by
which the numbers are calculated.

Definition
++++++++++

A prime number (or a prime) is a natural number that has exactly two
distinct natural number divisors: 1 and itself.

REFERENCE: http://en.wikipedia.org/wiki/Prime_number

Requirements
++++++++++++

The function should have the following signature::

 def primes(max=5):
    pass

Output
^^^^^^

The function should print to stdout, in the form of a comma
delimited list of numbers.

Correct answer
++++++++++++++

This is the expected correct answer::
 
 >>> primes(max=25)
 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
 67, 71, 73, 79, 83, 89, 97
