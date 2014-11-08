#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""

import datetime


class InvalidAgeError(Exception):
    """invalid age exception class"""

    pass


def get_age(birthyear):
    """determine age function"""

    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError
    return age

if __name__ == "__main__":
    print get_age(1985)
    print get_age(2099)