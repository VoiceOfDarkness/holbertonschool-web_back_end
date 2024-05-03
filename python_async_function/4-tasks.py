#!/usr/bin/env python3
"""
Tasks
"""
from typing import List
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return asyncio tasks
    """
    wait_list = [await task_wait_random(max_delay) for _ in range(n)]

    return wait_list
