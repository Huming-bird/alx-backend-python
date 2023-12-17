#!/usr/bin/env python3
"""Redefine wait_n to task_wait_n."""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times."""
    lis = []
    for i in range(n):
        res = await asyncio.gather(task_wait_random(max_delay))
        lis.extend(res)
    return sorted(lis)

print(asyncio.run(task_wait_n(3, 1)))