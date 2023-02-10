from gameclasses import Mage, Warrior


class Archer(Warrior):
    def __init__(self, health=100, stamina=100, arrows=20):
        super().__init__(health, stamina)
        self.arrows = arrows

    def attacks(self, target):
        print("----------------")
        print(f'{self.__class__.__name__} использует лук против {target.__class__.__name__}')
        target.health -= 4
        self.arrows -= 1
        print(f'Здоровье у {target.__class__.__name__} уменьшено до {target.health}\n'
              f'У {self.__class__.__name__} осталось {self.arrows} стрел')
        print("----------------")

    def introduces(self):
        super().introduces()
        print(f'Arrows: {self.arrows}')


class Alchemist(Mage):
    def __init__(self, health=10, mana=100, flasks=10):
        super().__init__(health, mana)
        self.flasks = flasks

    def attacks(self, target):
        print("----------------")
        print(f'{self.__class__.__name__} использует бутыль с огнем {target.__class__.__name__}')
        target.health -= 10
        self.health -= 3
        self.flasks -= 1
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}'
              f'Здоровье у {self.__class__.__name__} понижено до {self.health}\n'
              f'У {self.__class__.__name__} осталось {self.flasks} бутлей')
        print("----------------")


unit1 = Archer()
unit2 = Archer()
unit3 = Alchemist()

unit1.introduces()
unit3.attacks(unit1)
