import random

lil = ["Камень", "Ножницы", "Бумага"]
komp = random.choice(lil)
n = 0
kol_win = 0
kol_lose = 0

while kol_win < 3 or kol_lose < 3:
    player = input("Ваш ход:")
    answer = random.choice(lil)

    if player == "Камень" and answer == "Бумага":
        kol_lose += 1
        print("Мой ход:" + answer + ". У меня " + str(kol_lose) + "/3.")
    elif player == "Камень" and answer == "Ножницы":
        kol_win += 1
        print("Мой ход:" + answer + ". У вас " + str(kol_win) + "/3.")
    elif player == answer:
        print("Мой ход:" + answer + ". Ничья. Никто не получает очко.")
    elif player == "Ножницы" and answer == "Камень":
        kol_lose += 1
        print("Мой ход:" + answer + ". У меня " + str(kol_lose) + "/3.")
    elif player == "Ножницы" and answer == "Бумага":
        kol_win += 1
        print("Мой ход:" + answer + ". У вас " + str(kol_win) + "/3.")
    elif player == "Бумага" and answer == "Ножницы":
        kol_lose += 1
        print("Мой ход:" + answer + ". У меня " + str(kol_lose) + "/3.")
    elif player == "Бумага" and answer == "Камень":
        kol_win += 1
        print("Мой ход:" + answer + ". У вас " + str(kol_win) + "/3.")

if kol_win == 3 and kol_lose != 3:
    print("Вы победили!")
    print("Мой счёт " + str(kol_lose))
if kol_lose == 3 and kol_win != 3:
    print("Вы проиграли!")
    print("Ваш счёт " + str(kol_win))
if kol_lose == 3 and kol_win == 3:
    print("Ничья!")
    print("Ваш счёт " + str(kol_win) + "Мой счёт " + str(kol_lose))