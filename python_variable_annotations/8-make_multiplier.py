#!/usr/bin/env python3
"""
Make a multiplier
"""


def make_multiplier(multiplier: float) -> callable:
    """Return a function that multiplies a float by multiplier"""

    def multiply(n: float) -> float:
        """Multiply a float by multiplier"""

        return n * multiplier

    return multiply
