#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05: Custom Exception Class"""


class CustomError(Exception):
    """custom error"""

    def __init__(self, message, cause):
        Exception.__init__(self)
        self.message = message
        self.cause = cause