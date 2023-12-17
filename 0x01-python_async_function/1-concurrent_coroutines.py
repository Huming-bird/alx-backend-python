#!/usr/bin/env python3
"""A script that executes multiple coroutines at the same time with async."""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ 'n' times execution."""
    lis = []
    for i in range(n):
        res = await asyncio.gather(wait_random(max_delay))
        lis.extend(res)
    return sorted(lis)
