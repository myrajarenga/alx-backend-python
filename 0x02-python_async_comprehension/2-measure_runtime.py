#!/usr/bin/env python3
"""
run time for parallel comprehension
"""


import asyncio
from time import time


async def async_comprehension():
    """Async comprehesion"""


async def measure_runtime():
    """ measure time """
    start_time = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    total_runtime = time() - start_time
    return total_runtime
