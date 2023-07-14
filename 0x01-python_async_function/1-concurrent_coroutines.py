#!/usr/bin/env python3
"""asynchronous syntax with concurent execution"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = [
        asyncio.create_task(wait_random(max_delay))
        for _ in range(n)
    ]

    # Wait for all tasks to complete and gather the results
    completed_tasks = await asyncio.gather(*delays)

    return sorted(completed_tasks)
