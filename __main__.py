import random
import sys
import os
sys.path.append(os.getcwd()+"\entities")
from typing import List
from entities.soldier import Soldier
from entities.villager import Villager
from entities.farm import Farm

class Game:
    __soldiers : List[Soldier] = []
    def __init__(self) -> None:
        for i in range(10):
            self.__soldiers.append(
                Soldier(
                    health=100,
                    position=[
                        random.randint(0,100),
                        random.randint(0,100)
                    ],
                    speed=random.randint(0,3),
                    damage=random.randint(0,100)
                )
            )
        print(self.__soldiers)

Game()
