#!/usr/bin/env python3
""" Meaure runtime"""


import asyncio
import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure runtime in sec"""
    start_time = time.time()

    loop = asyncio.get_event_loop()
    delays = loop.run_until_complete(wait_n(n, max_delay))

    total_time = time.time() - start_time
    average_time = total_time / n

    return average_time

n = 5
max_delay = 3
result = measure_time(n, max_delay)
