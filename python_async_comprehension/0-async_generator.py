#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random

from typing import Generator, List


async def async_generator() -> Generator[List[float], None, None]:
    """
    coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)