from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1 import HealCapability, TransformCapability
from typing import cast


class InvalidStrategyException(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyException(f"Invalid Creature {creature.name}"
                                           "for normal strategy")
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyException(f"Invalid Creature {creature.name}"
                                           "for agressive strategy")
        return [cast(TransformCapability, creature).transform(),
                creature.attack(),
                cast(TransformCapability, creature).revert()]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyException(f"Invalid Creature {creature.name}"
                                           "for defensive strategy")
        return [creature.attack(), cast(HealCapability, creature).heal()]
