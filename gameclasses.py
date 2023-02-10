class Warrior:
    def __init__(self, health=100, stamina=100):
        self.health = health
        self.stamina = stamina

    def introduces(self):
        print("----------------")
        print(f'Class: {self.__class__.__name__}\n'
              f'Health: {self.health}\n'
              f'Stamina: {self.stamina}')
        print("----------------")

    def heals(self, target):
        print("----------------")
        print(f'{self.__class__.__name__} накладывает повязку из лечебных трав {target.__class__.__name__}')
        target.health += 10
        self.stamina -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}\n'
              f'У {self.__class__.__name__} осталось {self.stamina} выносливости')
        print("----------------")

    def attacks(self, target):
        print("----------------")
        print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print("----------------")


class Mage:
    def __init__(self, health=60, mana=100):
        self.health = health
        self.mana = mana

    def introduces(self):
        print("----------------")
        print(f'Class: {self.__class__.__name__}\n'
              f'Health: {self.health}\n'
              f'Mana: {self.mana}')
        print("----------------")

    def heals(self, target):
        print("----------------")
        print(f'{self.__class__.__name__} применяет заклинание лечения к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}\n'
              f'У {self.__class__.__name__} осталось {self.mana} маны')
        print("----------------")

    def attacks(self, target):
        print("----------------")
        print(f'{self.__class__.__name__} наносит урон магией {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print("----------------")





#unit1 = Warrior(25)
#unit2 = Warrior(stamina=120)
#unit3 = Mage()
#unit4 = Mage(health=50, mana=110)

#unit1.introduces()
#unit4.introduces()

#unit4.heals(unit1)

#unit1.introduces()
#unit4.introduces()
#unit1.attacks(unit4)

#print(unit1.__dict__)
#print(unit2.__dict__)
#print(unit3.__dict__)
