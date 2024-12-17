def anagramma(letter_1, letter_2):
    lt_1 = sorted(list(letter_1))
    lt_2 = sorted(list(letter_2))
    if lt_1 == lt_2:
        return 'Анаграмма'
    else:
        return 'не анаграмма'


letter_1 = input()
letter_2 = input()
print(anagramma(letter_1, letter_2))