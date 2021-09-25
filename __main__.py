import random
import sys
import os
sys.path.append(os.getcwd()+"/entities")
from entities.soldier import Soldier
from entities.villager import Villager
from entities.farm import Farm

class Main:
    def __init__(self) -> None:
        soldier : Soldier = Soldier(
            health=100,
            position=[
                random.randint(0,100),
                random.randint(0,100)
            ],
            speed=random.randint(0,3),
            damage=random.randint(0,100)
        )
        villager : Villager = Villager(
            health=100,
            position=[
                random.randint(0,100),
                random.randint(0,100)
            ],
            speed=random.randint(0,3),
        )
        harvest : int = villager.harvest(Farm())
        print(f'total harvested: {harvest} grains at {villager.position}')
        villager.walk([villager.position[0]+villager.speed, villager.position[1]])
        print(f'villager moved to {villager.position}')
        soldier.walk([villager.position[0]-1, villager.position[1]])
        print(f'moving soldier to {soldier.position}')
        print("soldier attacks a villager")
        while villager.health > 0:
            soldier.atack(villager)

Main()