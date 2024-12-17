def simple(chislo):
    for delitel in range(2, chislo, 1):
        if chislo % delitel == 0:
            return False
        else:
            return chislo


def find_simple(enter_1, enter_2):
    somelist = []
    for element in range(enter_1, enter_2 + 1):
        if simple(element) and element % 3 != 0 and \
            element % 5 != 0 and element % 7 != 0:
            somelist.append(element)
    return somelist


enter_1 = int(input())
enter_2 = int(input())
print(find_simple(enter_1, enter_2))
