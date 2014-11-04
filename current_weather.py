#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 11, current_weather file"""

import urllib2
import json

base_url = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city, country, units='metric'):
    api_query = '{}?units={}&q={},{}'.format(
        base_url, units, city, country
    )

    response = urllib2.urlopen(api_query)

    return json.load(response)['main']


print get_weather('New York', 'us')
print get_weather('San Francisco', 'us')
print get_weather('Austin', 'us')
