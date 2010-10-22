==========
Reflection
==========

Goal
++++

Consume input data and execute code based on the iput data itself.

Definition
++++++++++

There are many times when reflection is a useful design pattern.  A
very obvious use case for this is data driven tests.  In this
question you will be provided a class, and input data.  You need to
execute the method specified in the data, on the class.

REFERENCE: http://en.wikipedia.org/wiki/Reflection_%28computer_science%29

Requirements
++++++++++++

You are provided the following class::

 class Printer(object):
     def upper(self, text):
         print text.upper()

     def lower(self, text):
         print text.lower()

     def capitalize(self, text):
         print text.capitalize()

You are then given the following structure::

 data = [
    ('upper', 'Hello world'),
    ('lower', 'Hello world'),
    ('capitalize', 'Hello world')
 ]

Iterate over the data and for each row execute the ``Printer()``
method specified by the first dimension, passing in the value from the
second dimension.

Output
^^^^^^

The output is controlled by the ``Printer()`` class.

Correct answer
++++++++++++++

This is the one possible correct answer::

 >>> printer = Printer()
 >>> for method, text in data:
 ...     getattr(printer, method)(text)
 ...
 HELLO WORLD
 hello world
 Hello world
