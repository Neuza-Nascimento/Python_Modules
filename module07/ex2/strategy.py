from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1 import (TransformCreatureFactory, HealingCreatureFactory,
                 HealCapability, TransformCapability)
from typing import cast

class InvalidStrategyException(Exception):
    def __init__(self, msg = "Error") -> None:
        super().__init__(msg)


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature):
        pass

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
            return True
        
    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise InvalidStrategyException("Invalid Creature for normal strategy")
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
            return isinstance(creature, TransformCapability)
        
    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise InvalidStrategyException("Invalid Creature for agressive strategy")
        creature


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
            return isinstance(creature, HealCapability)
    
    def act(self, creature: Creature):
        pass


