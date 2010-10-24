==========================
ROT13 encryption algorithm
==========================

Goal
++++

Create a function that implements the ROT13 algorithm.

Definition
++++++++++

ROT13 is an example of the Caesar [1]_ cipher, developed in ancient
Rome.  Applying ROT13 to a piece of text merely requires examining its
alphabetic characters and replacing each one by the letter 13 places
further along in the alphabet [2]_, wrapping back to the beginning if
necessary. A becomes N, B becomes O, and so on up to M, which becomes
Z, then the sequence continues at the beginning of the alphabet: N
becomes A, O becomes B, and so on to Z, which becomes M.  Only those
letters which occur in the English alphabet [3]_ are affected;
numbers, symbols, whitespace, and all other characters are left
unchanged. Because there are 26 letters in the English alphabet and
``26 = 2 x 13``, the ROT13 function is its own inverse: [4]_


REFERENCE: http://en.wikipedia.org/wiki/ROT13

Requirements
++++++++++++

The function should have the following signature::

 def rot13(msg):
    pass

Pass the following string through your function, and validate you get the
correct answer::

 clvagreivrj

Output
^^^^^^

The function should print the ROT13 version of the string passed, and
since this particular input string is already encryptd, you should get
back a particular string.

Correct answer
++++++++++++++

This is the expected correct answer::
 
 rot13('clvagreivrj')
 >>> pyinterview

Footnotes
+++++++++

.. [1] http://en.wikipedia.org/wiki/Caesar_cipher
.. [2] http://en.wikipedia.org/wiki/Alphabet
.. [3] http://en.wikipedia.org/wiki/English_alphabet
.. [4] http://en.wikipedia.org/wiki/Inverse_function
