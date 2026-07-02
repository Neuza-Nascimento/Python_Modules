from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = dark_spell_allowed_ingredients()
    valid = any(
        ingredient in ingredients.lower() for ingredient in valid_ingredients
    )
    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
