#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer argument:"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An asynchronous coroutine."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


print(asyncio.run(wait_random(2)))