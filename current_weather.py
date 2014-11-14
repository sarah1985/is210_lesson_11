#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 11, current_weather file"""

import urllib2
import json
import csv
import os


class CurrentWeatherException(Exception):
    """weather exception class"""

    def __init__(self, code, message):
        super.
        self.errno = code
        self.message = message


class CurrentWeather(object):
    """current weather class"""

    zip_codes = {}
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    def __init__(self, zipcode_data='zipcode_database.csv'):
        pass

    def get_weather(self, city, country, units='metric'):
        """get weather"""

        self.api_query = '{}?units={}&q={},{}'.format(
            base_url, units, city, country
        )

        try:
            self.response = urllib2.urlopen(api_query)
        except urllib2.HTTPError, error:
            raise CurrentWeatherException(
                error.code,
                'Error: {} {}'.format(error.code, error.msg))

    def read_csv(self, csv_path):
        """csv reader"""

        if os.path.exists(csv_path):

            try:
                input_file = csv.reader(open(csv_path, 'r'))

                for line in input_file:
                    zip_codes[line[0]] = {
                        'city': line[1],
                        'state': line[2],
                        'latitude': float(line[3]),
                        'longitude': float(line[4]),
                        'country': line[5]
                        }

            except IOError:
                if input_file is not None:
            finally:



    return json.load(response)['main']


print get_weather('New York', 'us')
print get_weather('San Francisco', 'us')
print get_weather('Austin', 'us')
