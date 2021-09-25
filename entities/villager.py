from farm import Farm
from typing import List
from character import Character

class Villager(Character):
    def __init__(self, health: int, position: List, speed: float) -> None:
        super().__init__(health, position, speed)

    def harvest(self, farm: Farm) -> int:
        return farm.harvest()