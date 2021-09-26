from typing import List
from character import Character

class Soldier(Character):
    __damage : int
    def __init__(self, health: int, position: List, speed: float, damage: int) -> None:
        super().__init__(health, position, speed)
        self.__damage = damage

    @property
    def damage(self) -> int:
        return self.__damage
        
    @damage.getter
    def damage(self) -> int:
        return self.__damage
    
    def atack(self, character : Character) -> None:
        character.receive_damage(self.__damage)