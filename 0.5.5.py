def schet(spisok):
    dict1 = {}
    for element in spisok:
        if element not in dict1.keys():
            dict1[element] = 1
        else:
            dict1[element] += 1
    return dict1


def maxim(dict2):
    dict3 = {}
    while dict2 != {}:
        for v in dict2.values():
            znach = dict2[min(dict2)]
        dict3[min(dict2)] = znach
        del dict2[min(dict2)]
    return dict3


spisok = ['apple', 'banana', 'orange', 'apple', 'apple', 'banana']
dict2 = schet(spisok)
print(maxim(dict2))
