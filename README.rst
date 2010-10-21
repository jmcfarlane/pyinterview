======================
Welcome to Pyinterview
======================

Pyinterview is a simple script that generates a static webpage of
various engineering questions, the kinds you probably want to brush up
on prior to an interview.

Dependencies
++++++++++++

This project depends on the following:

1. Python 2.6 or higher
2. Docutils 0.6 or higher
3. Git (just to fetch the source code)

Here's what you'd do to satisfy the above on any version of Ubuntu
greater than or including 8.04 (Hardy)::

 sudo apt-get install python-docutils
 sudo apt-get install git-core

Usage
+++++

First fetch the source code::

  git clone git://github.com/jmcfarlane/pyinterview.git Pyinterview
  cd Pyinterview

Then generate the interview quesions::

  python grill.py

Or you can generate them and launch your browser in one shot::

  python grill.py -b
