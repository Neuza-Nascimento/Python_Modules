#!/usr/bin/python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players: list = [
        'Alice', "bob", "Charlie",
        "dylan", "Emma", "Gregory", "john",
        "kevin", "Liam"
    ]
    print(f"Initia list of players: {players}")
    playersCapitalize: list = [x.capitalize() for x in players]
    playersOnly: list = [x for x in players if x[0].isupper()]
    print(f"New list with all names capitalized: {playersCapitalize}")
    print(f"New list of capitalized names only: {playersOnly}")
    scorePlayers: dict = {name: random.randint(1, 1000)
                          for name in playersCapitalize}
    print(f"\nScore dict: {scorePlayers}")
    media: float = round(sum(scorePlayers.values()) / len(scorePlayers), 2)
    print(f"Score average: {media}")
    highScore: dict = {name: score for name, score
                       in scorePlayers.items() if score > media}
    print(f"High scores: {highScore}")


if __name__ == "__main__":
    main()
