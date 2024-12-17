lil_music = ["Led Zeppelin Stairway to Heaven"]
lil_films = ["Marvel"]
lil_bussines = []

message = input("Чё тебе надо?")
if "музыку" in message:
    print("Я бы посоветовал вам:" + lil_music[0])
elif "фильм" in message:
    print("Я бы посоветовал вам:" + lil_films[0])
elif "список дел" in message:
    while message != "закончи":
        print(lil_bussines)
        if lil_bussines == []:
            lil_bussines = []
            message = input("Напишите ваш список дел или напишите:")
            lil_bussines.append(message)
            print(lil_bussines)
        message = input("Выберите команду закончи или очистить или добавить:")
        if "добавить" in message:
            message = input("Добавьте к списку дел ещё дела:")
            lil_bussines.append(message)
        elif "очистить" in message:
            lil_bussines = []

elif "сложи числа":
    str1 = input("Напишите список чисел через запятую:")
    lil = str1.split(",")
    lenn = 0
    for i in lil:
        lenn += 1
    summ = 0
    n = 0
    while n != lenn:
        summ += int(lil[n])
        n += 1
    print(summ)