from typing import List
from character import Character

class Soldier(Character):
    __damage : int
    def __init__(self, health: int, position: List, speed: float, damage: int) -> None:
        super().__init__(health, position, speed)
        self.__damage = damage
    
    def atack(self, character : Character) -> None:
        character.health -= self.__damage