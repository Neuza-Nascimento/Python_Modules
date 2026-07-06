#!/usr/bin/python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    creature = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    creaturePro = factory.create_evolved()
    print(creaturePro.describe())
    print(creaturePro.attack())
    print()


def testing_battle(factory1: CreatureFactory,
                   factory2: CreatureFactory) -> None:
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()
    print(c1.describe())
    print(" vs.")
    print(c2.describe())
    print(" fight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:
    test_factory(FlameFactory())
    test_factory(AquaFactory())
    testing_battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
