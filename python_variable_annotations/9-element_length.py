#!/usr/bin/env python3
"""
This module demonstrates how to use the length
of a list as a variable annotation.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing
    the elements of lst and their lengths"""

    return [(i, len(i)) for i in lst]
