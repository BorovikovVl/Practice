chis1 = int(input())
chis2 = int(input())
spisok = []


def nod(chis1, chis2):
    for delitel1 in range(2, chis1 + 1):
        for delitel2 in range(2, chis2 + 1):
            if delitel1 == delitel2 and chis1 % delitel1 == 0 and chis2 % delitel2 == 0:
                spisok.append(delitel1)
    return spisok[-1]


print(nod(chis1, chis2))