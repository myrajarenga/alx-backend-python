#!/usr/bin/env python3
"""
Async comprehension
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehesion returning 10  random number"""
    random_numbers = [num async for num in async_generator()]
    return random_numbers
