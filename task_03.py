#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        handled = []

        fhandler = open(self.logfilename, 'a')
        for index, entry in enumerate(self.msgs):
            fhandler.write(str(entry) + '\n')
            handled.append(index)

        fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
