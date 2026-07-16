#!/usr/bin/env python3

from collections.abc import Callable
from functools import wraps
from time import time, sleep
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


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception:
                    print("Spell failed, retrying..."
                          f"(attempt {i}/{max_attempts})")
                    continue
            return (f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.replace(' ', '').isalpha():
            return True
        else:
            return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball(power: int) -> str:
    sleep(0.1)
    if power < 10:
        return "It needs more power!"
    return "Fireball cast!"


@retry_spell(3)
def spell(value: str) -> str:
    int(value)
    return "Waaaaaaagh spelled !"


def main() -> None:
    print("Testing spell timer..")
    print(f"Result: {fireball(10)}")
    print("\nTesting retrying spell...")
    print(spell("abc"))
    print(spell("42"))
    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name("Neuz02"))
    print(mage.validate_mage_name("Neuz AAA"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
