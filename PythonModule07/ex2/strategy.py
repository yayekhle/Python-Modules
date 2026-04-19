from abc import ABC, abstractmethod


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature):
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature):
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return hasattr(creature, "transform")

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' for this "
                "aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' for "
                "this defensive strategy"
            )

        print(creature.attack())
        print(creature.heal())
