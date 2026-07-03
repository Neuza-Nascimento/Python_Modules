#!/usr/bin/python3

from ex1 import (TransformCreatureFactory, HealingCreatureFactory,
                 HealCapability, TransformCapability)
from ex0 import CreatureFactory
from typing import cast


def healing_capability(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    c1 = factory.create_base()
    print(c1.describe())
    print(c1.attack())
    print(cast(HealCapability, c1).heal())
    print(" evolved:")
    c2 = factory.create_evolved()
    print(c2.describe())
    print(c2.attack())
    print(cast(HealCapability, c2).heal())
    print()


def transform_capability(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    c1 = factory.create_base()
    print(c1.describe())
    print(c1.attack())
    print(cast(TransformCapability, c1).transform())
    print(c1.attack())
    print(cast(TransformCapability, c1).revert())
    print(" evolved:")
    c2 = factory.create_evolved()
    print(c2.describe())
    print(c2.attack())
    print(cast(TransformCapability, c2).transform())
    print(c2.attack())
    print(cast(TransformCapability, c2).revert())


def main() -> None:
    healing_capability(HealingCreatureFactory())
    transform_capability(TransformCreatureFactory())


if __name__ == "__main__":
    main()
