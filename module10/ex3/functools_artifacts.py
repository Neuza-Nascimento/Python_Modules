#!/usr/bin/env pyhton3

import operator
from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    result: int = 0
    if len(spells) == 0:
        return 0
    elif operation == "add":
        result = reduce(operator.add, spells)
    elif operation == "multiply":
        result = reduce(operator.mul, spells)
    elif operation == "max":
        result = max(spells)
    elif operation == "min":
        result = min(spells)
    else:
        print("Operation not supported")
        return 0
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {"fire": partial(base_enchantment, 50, "fire"),
            "ice": partial(base_enchantment, 50, "ice"),
            "lightning": partial(base_enchantment, 50, "lightning")}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell) -> str:
        return f"Enchatment: {spell}"

    @dispatch.register(list)
    def _(spell) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def main() -> None:
    spell_powers = [34, 22, 10, 49, 38, 47]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [0, 1, 10, 15]
    print("Testing spell reducer...")
    for op in operations:
        print(f"Operation {op}: {spell_reducer(spell_powers, op)}")
    print("\nTesting memoized fibonacci...")
    for test in fibonacci_tests:
        print(f"Fib({test}): {memoized_fibonacci(test)}")
    print(memoized_fibonacci.cache_info())
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher((1, 2)))


if __name__ == "__main__":
    main()
