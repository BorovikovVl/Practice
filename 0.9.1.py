name_pet = input()
type_pet = input()
age_pet = input()
print('    ')


def new_pet(name_pet, type_pet, age_pet):
    print('Новый питомец создан!')


def function_pet(name_pet):
    print('Надо бы поухаживать за питомцем', name_pet)
    print('Выберите действие: играть, покормить или уложить спать')
    word = input()

    if 'играть' in word:
        k = 6
        while k != 1:
            k -= 1
            print(k)
        print('Питомец с кайфом поиграл')

    elif 'покормить' in word:
        k = 6
        while k != 1:
            k -= 1
            print(k)
        print('Питомец с кайфом поел')

    elif 'спать' in word:
        k = 11
        while k != 1:
            k -= 1
            print(k)
        print('Питомец с кайфом поспал')


def vibe_pet(name_pet):
    word = input()

    hungry = 0
    happy = 5
    energy = 5

    if 'играть' in word:
        happy += 1
        hungry -= 2
        if energy >= 4:
            energy -= 1
        if energy <= 2:
            print('Питомец поиграл')

    if 'спать' in word:
        if energy < 5:
            print('Питомец не хочет спать')
        if energy >= 1:
            energy -= 1

    if 'покормить' in word:
        happy -= 1
        energy += 1
        if hungry < 2:
            print('Питомец сыт')
        if hungry >= 2:
            hungry -= 1

    print('Голод: ', hungry, 'Радость: ', happy, 'Энергия: ', energy)


print(new_pet(name_pet, type_pet, age_pet))
print(function_pet(name_pet))
print(vibe_pet(name_pet))
