#!/usr/bin/env python3
"""
Async generator
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> [float, NoneType, NoneType]:

    """coroutine called async generator loop 10 times wait  sec"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
