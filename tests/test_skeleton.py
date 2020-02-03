# -*- coding: utf-8 -*-

import pytest
from awr_python.skeleton import fib

__author__ = "Patrick Boulay"
__copyright__ = "Patrick Boulay"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
