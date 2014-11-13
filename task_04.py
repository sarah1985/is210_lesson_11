#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04: Exception Class Hierarchies"""


class BaseException(Exception):
    """new exception classes"""


class StringError(BaseException, TypeError):
    """new string error"""


class NumberError(BaseException, TypeError):
    """new number error"""


class NonZeroError(NumberError):
    """non-zero error"""