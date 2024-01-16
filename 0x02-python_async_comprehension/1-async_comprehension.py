#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine will collect 10 random numbers using an
        async comprehensing then return the 10 random numbers"""
    rand_list = [i async for i in async_generator()]
    return rand_list
