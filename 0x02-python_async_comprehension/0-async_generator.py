#!/usr/bin/env python3
"""
Async generator
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> [float, None, None]:

    """coroutine called async generator loop 10 times wait  sec"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
