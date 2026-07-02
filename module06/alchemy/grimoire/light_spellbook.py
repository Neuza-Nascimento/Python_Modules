from .light_validator import validate_ingredients


__all__ = ["light_spell_allowed_ingredients", "light_spell_record"]


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    value = validate_ingredients(ingredients)
    if "VALID" in value:
        return f"Spell recorded: {spell_name} {value}"
    return f"Spell rejected: {spell_name} {value}"
