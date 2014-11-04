==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #11
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-11-10T09:00:00-0400
:Due-Date: 2014-11-17T09:00:00-0400

Overview
========

This week, we learn about a pillar of the pantheon of Python programming
paradigms: exceptions. Throughout this assignment you will be challenged
to both use and consider the use of exceptions as a control mechanisms
withing your programs.

Warm-Up Tasks
=============

Task 01: Simple Exception Handling
----------------------------------

In this exercise you'll be adding exception handling to a function that
already exists.

Specifications
^^^^^^^^^^^^^^

#.  Open ``task_01.py``

#.  Add exception handling to the ``simple_lookup()`` function so that
    attempts to access any index or key of ``var1`` that do not exist will
    print a warning message and return ``var1``

#.  Allow all other exceptions to fail normally.

.. tip::

    There is a single exception class that suits this best.
    
Example
^^^^^^^

.. code:: pycon

    >>> simple_lookup([1,2], 4)
    Warning: Your index/key doesn't exist.
    [1,2]
    >>> simple_lookup({}, 'banana')
    Warning: Your index/key doesn't exist.
    {}

Task 02: Raise a Manual Exception
---------------------------------

In this exercise, you'll raise a manual exception when a condition is not
met in a particular function. In particular, we'll be converting birth year to
age.

Specifications
^^^^^^^^^^^^^^

#.  Open ``task_02.py``

#.  Add a check that tests whether or not the person has a valid (0 or greater)

#.  If the age is invalid, raise an ``InvalidAgeError``

Examples
^^^^^^^^

.. code:: pycon

    >>> get_age(2099)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    __main__.InvalidAgeError

Task 03: Using Finally
----------------------

The ``finally`` clause is particularly useful in handling cleanup tasks such
as closing file descriptors or data streams.

Specifications
^^^^^^^^^^^^^^

#.  Open ``task_03.py``. This class represents a very simple logging class.
    Python offers much-better built-in loggers but this is a good teaching
    example.

#.  Modify ``flush()`` so that any predictable errors are caught and are,
    themselves, logged.

    #.  If the target logfile cannot be opened, log this fact then re-raise
        the error.

    #.  Upon encountering any other ``IOError``, log the error and stop loop
        loop processing (but continue with the rest of the program)

    #.  Do not allow stored messages to be removed from the ``msgs`` object if
        they cannot be written to the disk.

    #.  Allow msgs processing to continue as long as it doesn't encounter an
        ``IOError``

    #.  Upon encountering any other error, use the ``log()`` method to log the
        error encountered

#.  Ensure that the ``close()`` method is called no matter what exceptions are
    encountered.

.. note::

    Unit testing will be limited in this particular question as exception
    handling largely defeats changes in program state and, to be frank, Python
    is just really good with polymorphism. There's almost nothing that can
    trigger an exception with str()!

Task 04: Exception Class Hierarchies
------------------------------------

Creating custom exception classes is a major part of any programming project.

#.  Create a file named ``task_04.py``

#.  Create a new exception class named ``BaseException`` which simply extends
    ``Exception``

#.  Create three additional exception classes with the following hierarchies:

    #.  ``StringError``, subclassed to ``BaseException`` and ``TypeError``

    #.  ``NumberError``, subclassed to ``BaseException` and ``TypeError``

    #.  ``NonZeroError``, subclassed to ``NumberError``

Task 05: Custom Exception Classes
---------------------------------

A custom exception class can sometimes offer important additional functionality
in debugging errors.

#.  Create a file named ``task_05.py``

#.  Create a custom exception class named ``CustomError`` that is subclassed
    to ``Exception``

#.  ``CustomError`` has a custom constructor that calls
    ``Exception.__init__()`` but also takes a third parameter named ``cause``
    and stores its value as ``self.cause``

Task 06: Handling Multiple Exceptions Together
----------------------------------------------

Except clauses may match multiple types of exceptions saving unnecessary
duplication and effort.

#.  Open ``task_06.py``

#.  Alter the ``except`` clause so that it catches ``TypeError``, ``KeyError``,
    and ``IndexError``

    #.  Do not add additional except clauses!

#.  Allow any other exceptions to occur naturally

.. tip::

    Check out Python's exceptions documentation for a neat way to capture both
    ``KeyError`` and ``IndexError`` in the same superclass.

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Lesson 01.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
