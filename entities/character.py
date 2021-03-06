from typing import List

class Character: 
    __health : int = 100
    __position : List = [0,0]
    __speed : float = 10

    def __init__(self, health : int, position: List, speed: float) -> None:
        self.__health = health
        self.__position = position
        self.__speed = speed

    def __del__(self):
        pass

    @property
    def position(self) -> List:
        return self.__position

    @property
    def health(self) -> int:
        return self.__health

    @property
    def speed(self) -> float:
        return self.__speed

    @position.getter
    def position(self) -> List:
        return self.__position

    @health.getter
    def health(self) -> int:
        return self.__health

    @speed.getter
    def speed(self) -> float:
        return self.__speed
    
    @speed.setter
    def speed(self, speed : int) -> None:
        self.__speed = speed

    @health.setter
    def health(self, health: int) -> None:
        self.__health = health
        if self.__health <= 0:
            print("character is dead")
    
    @position.setter
    def position(self, x: int, y: int) -> None:
        self.__position = [x,y]

    def receive_damage(self, damage : int) -> None:
        self.health -= damage

    def walk(self,position: List) -> None:
        self.__position = position