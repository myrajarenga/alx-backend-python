#!/usr/bin/env python3
"""function that takes afunction and returns afunction"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """func that takes in a function and return a function"""
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
