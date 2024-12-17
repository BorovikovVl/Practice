import random

name_hero = input('Введите имя героя: ')
armor = ['стальная броня', 'алмазная броня', 'бронижилет']
weapon = ['меч', 'пистолет', 'огнемет']
hp_hero = [50, 100, 150, 200]
damage_hero = [20, 35, 60]

inf_hero = {'Допспехи': random.choice(armor),
            'Оружие': random.choice(weapon),
            'Здоровье': random.choice(hp_hero),
            'Урон': 'от 20 до 60'
            }

name_dragon = input('Введите имя дракона: ')
hp_dragon = [200, 300, 350]
damage_dragon = [10, 30, 70]

inf_dragon = {'Здоровье': random.choice(hp_dragon),
              'Урон': 'от 10 до 70'}


def fight(dam_hero, dam_dragon, health_hero, health_dragon):
    while health_hero > 0 and health_dragon > 0:
        health_dragon -= dam_hero
        print(f'Здоровье дракона: {health_dragon}')

        if health_dragon <= 0:
            print('Победил герой!')
            break

        health_hero -= dam_dragon
        print(f'Здоровье героя: {health_hero}')

        if health_hero <= 0:
            print('Победил дракон!')
            break


dam_hero = random.choice(damage_hero)
dam_dragon = random.choice(damage_dragon)

print(f'Однажды один герой по имени {name_hero} нашел себе оружие, доспехи, накачался и пошел в бой с драконом {name_dragon}')

fight(dam_hero, dam_dragon, inf_hero['Здоровье'], inf_dragon['Здоровье'])