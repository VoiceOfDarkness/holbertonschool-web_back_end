#!/usr/bin/env python3
"""
return a tuple containing the square of the first argument and the square of
the second argument
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return a tuple containing the square of the first argument
    and the square of
    the second argument
    """
    return (k, v * v)
