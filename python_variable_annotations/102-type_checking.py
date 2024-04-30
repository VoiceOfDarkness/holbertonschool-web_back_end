#!/usr/bin/env python3
"""
This module demonstrates how to use type checking in Python.
"""
from typing import Tuple


def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int]:
    """
    zoom_array takes a tuple of integers and returns a new tuple
    """

    zoomed_in = [item for item in lst for i in range(factor)]
    return tuple(zoomed_in)


array = (12, 72, 91)
zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
