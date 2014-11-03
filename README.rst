==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #10
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-11-03T09:00:00-0400
:Due-Date: 2014-11-10T09:00:00-0400

Overview
========

This exercise will have you interacting with several files. You'll create a
series of functions that will correlate two data sources then write your output
to a report.

Checking the Weather
====================

Tasks 7 -
-------------

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

#.  Create a constructor for ``CurrentWeather``

#.  In the constructor, create an *instance attribute* named ``zip_codes`` and
    assign it an empty dictionary object

#.  Add a second *instance attribute* named ``base_url`` and assign it a
    string value of ``http://api.openweathermap.org/data/2.5/weather``.

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

#.  For the ``except`` event code, simply use ``pass`` for now as a place holder
. You will be modifying this portion of
    the code in the next task.

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
