class Knight():
    def __init__(self, k_damage, k_hp):
        self.k_damage = k_damage
        self.k_hp = k_hp

    def knights(self):
        return f'Health: {self.k_hp}  and   Damage: {self.k_damage}'


class Dragon():
    def __init__(self, dr_damage, dr_hp):
        self.dr_damage = dr_damage
        self.dr_hp = dr_hp

    def dragons(self):
        return f'Health: {self.dr_hp}  and   Damage: {self.dr_damage}'


class Crazy_Mega_Fight():
    def __init__(self, k_hp, dr_hp, k_damage, dr_damage):
        self.k_hp = k_hp
        self.dr_hp = dr_hp
        self.k_damage = k_damage
        self.dr_damage = dr_damage

    def fight(self):
        while int(self.dr_hp) > 0 or int(self.k_hp > 0):
            print('Лее ударьего да (напиши "бей")')
            punch = input()
            self.dr_hp = int(self.dr_hp) - int(self.k_damage)
            print(f'Хороший удар! У дракона осталась {self.dr_hp} хп')
            print('Защищайся!')
            self.k_hp = int(self.k_hp) - int(self.dr_damage)
            print('норм попал так то')
            print(f'У тебя осталось {self.k_hp} хп')

        if self.dr_hp == 0:
            print('YOU LOSE')
        else:
            print('YOU WIN')


knight = Knight('120', '100')
dragon = Dragon('10', '1000')
fights = Crazy_Mega_Fight('100', '1000', '120', '10')

print(knight.knights())
print(dragon.dragons())
print(fights.fight())
