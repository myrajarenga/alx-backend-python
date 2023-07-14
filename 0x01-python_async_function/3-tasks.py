#!/usr/bin/env python3
import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random
"""returns a asyncio.Task"""


def task_wait_random(max_delay: int) -> Task:
    '''Return asynchronous taska'''
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
