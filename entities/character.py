from typing import List

class Character: 
    __health : int = 100
    __position : List = [0,0]
    __speed : float = 10

    def __init__(self, health : int, position: List, speed: float) -> None:
        self.__health = health
        self.__position = position
        self.__speed = speed

    @property
    def position(self) -> List:
        return self.__position

    @property
    def health(self) -> int:
        return self.__health

    @property
    def speed(self) -> float:
        return self.__speed
    
    @speed.setter
    def speed(self, speed : int) -> None:
        self.__speed = speed

    @health.setter
    def health(self, health: int) -> None:
        self.__health = health
    
    @position.setter
    def position(self, x: int, y: int) -> None:
        self.__position = [x,y]

    def receive_attack(self) -> None:
        self.__position
        pass

    def walk(self,position: List) -> None:
        self.__position = position