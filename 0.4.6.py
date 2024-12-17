def cesar(string, alfabet):
    new_list = []
    for i in string:
        new_list.append(i)

    new_string = ''

    for letter in new_list:
        letter = int(alfabet.index(letter)) + 2
        new_string += str(alfabet[letter])

    return new_string


def anticesar(string, alfabet):
    new_list = []
    for i in string:
        new_list.append(i)

    new_string = ''

    for letter in new_list:
        letter = int(alfabet.index(letter)) - 2
        new_string += str(alfabet[letter])

    return new_string


alfabet = sorted('йцукенгшщзхъэждлорпавыфячсмитьбю')
string = input()
'''print(cesar(string,alfabet))'''
print(anticesar(string, alfabet))