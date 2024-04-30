#!/usr/bin/env python3
"""
This module demonstrates how to safely get a value from a dictionary.
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """
    Safely return the value of a key from a dictionary
    """

    if key in dct:
        return dct[key]
    else:
        return default
