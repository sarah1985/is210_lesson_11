#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01: Simple Exception Handling"""


def simple_lookup(var1, var2):
    """exception handling practice"""

    try:
        return var1[var2]
    except LookupError:
        print 'Warning: your index/key doesn\'t exist.'
    print var1

if __name__ == "__main__":
    print simple_lookup([1, 2], 4)
    print simple_lookup({}, 'banana')