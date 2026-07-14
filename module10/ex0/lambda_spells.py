#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]
    avg_power = sum(map(lambda x: x["power"], mages)) / len(mages)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": round(avg_power, 2),
    }


def main() -> None:
    artifacts = [
        {"name": "Ice Wand", "power": 79, "type": "weapon"},
        {"name": "Wind Cloak", "power": 69, "type": "weapon"},
        {"name": "Earth Shield", "power": 101, "type": "relic"},
        {"name": "Storm Crown", "power": 74, "type": "armor"},
    ]

    mages = [
        {"name": "Sage", "power": 99, "element": "earth"},
        {"name": "Riley", "power": 65, "element": "lightning"},
        {"name": "Morgan", "power": 60, "element": "lightning"},
        {"name": "Storm", "power": 54, "element": "wind"},
        {"name": "Sage", "power": 98, "element": "water"},
    ]

    spells = ["tsunami", "darkness", "earthquake", "tornado"]
    print("\nTesting artifact sorter...")
    print(artifact_sorter(artifacts))

    print("\nTesting spell transformer...")
    print(spell_transformer(spells))

    print("\nTesting Power Filter...")
    print(power_filter(mages, 50))

    print("\nTesting Mage Stats")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
