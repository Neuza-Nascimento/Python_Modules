#!/usr/bin/python3

from ex2 import (BattleStrategy, NormalStrategy, DefensiveStrategy,
                 AggressiveStrategy, InvalidStrategyException)
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    tam = len(opponents)
    print(f"{tam} opponents involved\n")
    for j in range(tam):
        for i in range(j + 1, tam):
            opponent1, strategy1 = opponents[j]
            opponent2, strategy2 = opponents[i]
            print("\n* Battle *")
            print(opponent1.describe())
            print("  vs.")
            print(opponent2.describe())
            print("now fight!")
            try:
                for result in strategy1.act(opponent1):
                    print(f"{result}")
                for result in strategy2.act(opponent2):
                    print(f"{result}")
            except InvalidStrategyException as e:
                print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    flame = FlameFactory().create_base()
    aqua = AquaFactory().create_base()
    transf = TransformCreatureFactory().create_base()
    heald = HealingCreatureFactory().create_base()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    agressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (heald, defensive)])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, defensive), (heald, defensive)])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aqua, normal), (heald, defensive), (transf, agressive)])


if __name__ == "__main__":
    main()
