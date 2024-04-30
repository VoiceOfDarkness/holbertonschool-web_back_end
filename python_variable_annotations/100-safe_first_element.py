#!/usr/bin/env python3
"""
first_element of sequence
"""
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of lst if it exists, otherwise None"""

    if lst:
        return lst[0]
    else:
        return None
