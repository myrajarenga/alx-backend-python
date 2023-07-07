#!/usr/bin/env python3
"""anotated function that takes int and str and returns atuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function that takes int and str and returns atuple"""
    return k, float(v ** 2)
