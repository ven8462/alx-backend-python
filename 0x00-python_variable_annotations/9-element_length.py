#!/usr/bin/env python3
"""  duck typing on an iterable object """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with the length of each element
    """
    return [(i, len(i)) for i in lst]
