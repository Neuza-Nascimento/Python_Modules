from alchemy.grimoire import light_spell_record


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing lead to gold: "
          f"{light_spell_record('Fantasy', 'Earth, wind and fire')}")


if __name__ == "__main__":
    main()
