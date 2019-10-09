"""
Test helloworld script
"""

from helloworld import devide
import pytest

def test_devide():
    """
    Test devide(x, y) Function
    """
    assert devide(10,5) == 2
