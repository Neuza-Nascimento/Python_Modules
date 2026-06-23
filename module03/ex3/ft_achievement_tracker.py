#!/usr/bin/python3

import random


def gen_player_achievements(achievements: list, number: int) -> set[str]:
    choises = random.sample(achievements, number)
    return set(choises)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print("")
    achievements = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable",
        "Boss Slayer", "Strategist", "Unstoppable", "Speed Runner",
        "Survivor", "Treasure Hunter", "First Steps", "Sharp Mind"
    ]
    all_achievements: set = set(achievements)
    alice = gen_player_achievements(achievements, 6)
    bob = gen_player_achievements(achievements, 7)
    charlie = gen_player_achievements(achievements, 9)
    dylan = gen_player_achievements(achievements, 5)
    print(f"PLayer Alice: {alice}")
    print(f"PLayer Bob: {bob}")
    print(f"PLayer Charlie: {charlie}")
    print(f"PLayer Dylan: {dylan}")
    print("\nAll distint achievements:"
          f"{set.union(alice, charlie, bob, dylan)}")
    print(f"\nCommon achivements: {alice.intersection(bob, charlie, dylan)}")
    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}")
    print(f"\nAlice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
