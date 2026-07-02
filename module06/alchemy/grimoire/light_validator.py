def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    valid_ingredients = light_spell_allowed_ingredients()
    valid = any(
        ingredient in ingredients.lower() for ingredient in valid_ingredients
    )
    status = "VALID" if valid else "INVALID"
    return f"({ingredients} - {status})"
