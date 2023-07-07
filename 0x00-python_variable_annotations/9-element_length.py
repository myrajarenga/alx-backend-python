#!/usr/bin/env python3
"""anotating function parameters"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """anotatng function parameters"""
    return [(i, len(i)) for i in lst]
