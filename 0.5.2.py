def summm(spisok):
    spisok = elem.split()
    summ_polozh = 0
    for i in spisok:
        if int(i) % 2 == 0:
            summ_polozh += int(i)
    else:
        summ_polozh += 0
    return summ_polozh


spisok = []
elem = input('Введите список чисел через пробел: ',)
print(summm(spisok))
