#!/usr/bin/env python3
"""using the  asyncio and random module"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(times: int, max_delay: int) -> List[float]:
    """Runs the wait_random coroutine a certain number of times
      with a delay between each run.

    Args:
        times: The number of times to run the wait_random coroutine.
        max_delay: The maximum delay in seconds between each run.

    Returns:
        A list of the delays used in each run.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(times)]
    return [await task for task in asyncio.as_completed(tasks)]
