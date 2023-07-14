#!/usr/bin/env python3
"""more tasks """


import asyncio
from typing import List
from heapq import nsmallest
task_wait_random = __import__('3-tasks').task_wait_random
"""uses task_wait_random"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """anschronous tasks"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return nsmallest(n, results)
