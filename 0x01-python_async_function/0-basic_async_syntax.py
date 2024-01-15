#!/usr/bin/env python3
"""using the  asyncio and random module """

import asyncio
import random


async def wait_random(max_delay=10):
    """
    an asynchronous coroutine that takes in an integer argument,
    delays it for some time and returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
