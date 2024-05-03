#!/usr/bin/env python3
"""
return asyncio tasks
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    return asyncio tasks
    """
    return asyncio.Tasl(wait_random(max_delay))
