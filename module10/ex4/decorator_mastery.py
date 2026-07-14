#!/usr/bin/env python3

from collections.abc import Callable
from functools import wraps
from time import time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    print(f"Casting {func.__name__}...")

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        duration = time()
        res = func(*args, **kwargs)
        duration1 = time() - duration
        print(f"Spell completed in {duration1:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = args[-1]
            if value >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def main() -> None:
    pass


if __name__ == "__main__":
    main()