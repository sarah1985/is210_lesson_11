#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Using Finally"""


import time


class CustomLogger(object):
    """customer logger docstring"""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """log docstring"""

        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """flush docstring"""

        handled = []

        try:

            fhandler = open(self.logfilename, 'a')

            try:
                for index, entry in enumerate(self.msgs):
                    fhandler.write(str(entry) + '\n')
                    handled.append(index)

            except IOError:
                raise self.log('input output error')

            finally:
                fhandler.close()

        except BaseException:
            raise self.log('other error')
        try:
            for index in handled[::-1]:
                del self.msgs[index]
        except IOError:
            pass