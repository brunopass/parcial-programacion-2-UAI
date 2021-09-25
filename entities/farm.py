import random

class Farm:
    __food : int = random.randint(0,1000)

    def __init__(self) -> None:
        pass

    @property
    def food(self) -> int:
        return self.__food

    @food.setter
    def food(self, food) -> None:
        self.__food = food

    def harvest(self) -> int:
        harvest = random.randint(0,self.__food)
        self.__food-=harvest
        return harvest