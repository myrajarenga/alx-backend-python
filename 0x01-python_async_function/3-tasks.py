#!/usr/bin/env python3
import asyncio
from asyncio import Task
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random
"""returns a asyncio.Task"""


def task_wait_random(max_delay: int) -> Any:
    '''Return asynchronous taska'''
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
