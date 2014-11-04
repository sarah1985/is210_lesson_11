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

Checking the Weather
====================

This assignment involves using a RESTful online API to check the weather for
major U.S. cities by zip code. Since web service APIs are not something
directly covered in this course, we've gone a head and provided you with a
working starter file. Pretend it was written by your overworked senior systems
administrator as he was commuting in to work on the rail road. It's not
pretty but it works and is enough to get you started.

Your task is to improve the file by turning it into a Python class complete
with exception handling. You also need to add some additional functionality.
The weather API service only accepts the name of cities and their country.
The application this module is destined for will need to lookup the weather
by U.S. zipcode. You must add methods to the class that allow the class to
read from a CSV file which has zip codes and matching city names,
look up the zip code and return the matching city.


Task 7: Convert the File to Class
---------------------------------

The first thing you need to do is create a class named ``CurrentWeather`` to
hold the methods.

Specifications
^^^^^^^^^^^^^^

#.  Create a class named ``CurrentWeather``.

#.  Create an *instance attribute* named ``zip_codes`` and
    assign it an empty dictionary object

#.  Add a second *instance attribute* named ``base_url`` and assign it a
    string value of ``http://api.openweathermap.org/data/2.5/weather``.

#.  Create a constructor for ``CurrentWeather``

    #.  The constructor function should accept a variable named
        ``zipcode_data`` with a default value of ``zipcode_database.csv``.

    #.  Add a ``pass`` statement as a temporary stand in for code you will
        add in a following task.

Task 8: Move Existing Function Into Class
-----------------------------------------

Now you will need to move the existing ``get_weather()`` function into the
new class. Then consider the lack of exception handling in the current
version of the function. How will the class handle a situation where the
``urllib2.urlopen()`` object function call fails? Add some exception handling
to the method.

.. note::

    Don't forget to add the ``self`` object variable as the first argument of
    the ``get_weather()`` once you migrate it into the ``CurrentWeather``
    class

#.  Move the existing ``get_weather()`` function into the new class. Be sure
    to make the appropriate changes to the method.

#.  Wrap the ``response = urllib2.urlopen(api_query) in a ``try`` block. For
    the ``except`` exception use ``except urllib2.HTTPError, error:``

#.  For the ``except`` event code, simply use ``pass`` for now as a place
    holder . You will be modifying this portion of the code in the next task.

Task 9: Create General Exception Helper Class
---------------------------------------------

Sub-classing the basic Python ``Exception`` class is very common method for
creating custom exceptions for class objects. Create a
``CurrentWeatherException`` class that accepts two arguments as part of its
instantiation constructor.

Specifications
^^^^^^^^^^^^^^

#.  Create a class named ``CurrentWeatherExpection`` that sub-classes the
    standard ``Exception`` class.

#.  Overload the constructor method so that it accepts two arguments.

    #.  Argument one should be a variable named ``code``

    #.  The second arguments must be a variable named ``message``

    #.  Use the new-style classes method ``super`` to inherit the base class
        initialization method. This must directly follow the `def` line.

    #.  Assign the ``code`` value to an *instance attribute* named ``errno``.

    #.  Assign the ``message`` value to the *instance attribute* named
        ``message``.

#.  Update the ``get_weather()`` method to use this exception class. Replace
    the ``pass`` statement with the following code.

.. code-block:: pycon

    raise CurrentWeatherException(
        error.code,
        'Error: {} {}'.format(error.code, error.msg)
    )

Task 10: Create a CSV Reader Method
-----------------------------------

This portion of the assignment builds on the work you did last week for
reading CSV files. This time you will need to add exception handling
statements. Use your previous code here inside a function named
``read_csv()``. The function must accept a variable named ``csv_path``.

Specifications
^^^^^^^^^^^^^^

#.  Create a function within the class named ``read_csv()`` that accepts an
    argument named ``csv_path``.

#.  Use your CSV reading work from Lesson 10 task 01. Add the following
    exception handling

    #.  Use a conditional statement ``os.path.exists(csv_path)`` to detect if
        the CSV file is present. Raise an exception using the
        ``CurrentWeatherException`` class.

        #. code = 9010

        #. message = ``'CSV zipcode database {} not found'.format(csv_path)``

    #.  Wrap the CSV file ``open()`` function with a ``try`` block. Trap for
        ``IOError`` exceptions. Use the ``finally`` to close the file_object
        if it is not ``None``.

    #.  For the exception action, use the ``CurrentWeatherException`` class.

        #.  code = 4151

        #.  message = ``'Error reading {}'.format(csv_path))``

.. tip::

    You will need to loop through the contents of the CSV file while you are
    in the ``try`` block.

#.  Assign the zip as the key for the *instance attribute* named
    ``zip_codes``. For the value assign a dictionary object with the
    following keys: ``'city', 'state', 'latitude', 'longitude', 'country'``.

#.  Update the class constructor function to call this method at instatiation
    of the object.

Task 11: Create Method for Retrieving Cities
--------------------------------------------

Now you need to create a class method that searches through the zip code data
returns the name of the city that matches a particular zip code. It should
raise a ``CurrentWeatherException`` if it cannot find the zip code.

Specifications
^^^^^^^^^^^^^^

#.  Create a function within the class named ``get_city_by_zipcode()`` that
    accepts an argument named ``zipcode``.

#.  The function should throw a ``CurrentWeatherException`` in the event that
    the given zip code does not exists.

    #.  code = 5150

    #.  message = 'Error: Zipcode not found in Zipcode data.'

#.  Return only the ``city`` portion of the data

Task 12: Create Method for Retrieving Weather By Zip Code
---------------------------------------------------------

All of the heavy lifting is now done. Create a simple class method that
accepts a zip code and then calls the ``get_city_by_zipcode()`` and
``get_weather()`` methods.

Specifications
^^^^^^^^^^^^^^

#.  Create a function within the class named ``get_weather_by_zipcode()`` that
    accepts an argument named ``zipcode``.

#.  Return the weather dictionary output of the ``get_weather()`` method.

Example
-------

.. code-block::

    >>> from current_weather import CurrentWeather
    >>> cw = CurrentWeather()
    >>> cw.get_weather_by_zipcode('10001')
    {u'pressure': 1017, u'temp_min': 3, u'temp_max': 6, u'temp': 4.67, u'humidity': 44}
    >>> cw.get_weather_by_zipcode('60670')
    {u'pressure': 1022, u'temp_min': 8, u'temp_max': 10, u'temp': 9, u'humidity': 39}
    >>> cw.get_weather_by_zipcode('94101')
    {u'pressure': 1021, u'temp_min': 2, u'temp_max': 21, u'temp': 11.54, u'humidity': 77}
    >>>

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
