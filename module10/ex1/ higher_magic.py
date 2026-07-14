#!/usr/bin/env python3

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return res1, res2
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        res = base_spell(target, multiplier * power)
        return res
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def condicional(target: str, power: int) -> str:
        if condition(target, power):
            res = spell(target, power)
            return res
        else:
            return "Spell fizzled"
    return condicional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        res = [spell(target, power) for spell in spells]
        return res
    return sequence


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball restores {target} for {power} HP"


def condition(target: str, power: int) -> bool:
    if power < 10:
        return False
    else:
        return True


def main() -> None:

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 20)
    print(f"{result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Goblin", 10))

    print("\nTesting conditional caster...")
    conditional_spell = conditional_caster(condition, heal)
    print(conditional_spell("Ghost", 5))
    print(conditional_spell("Ghost", 20))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([heal, fireball, condition])
    print(sequence("Dragon", 15))


if __name__ == "__main__":
    main()
