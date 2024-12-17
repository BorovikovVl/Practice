numbers = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def summa(numbers):
    summ = 0
    for element in numbers:
        summ += element

    return summ


def mean(numbers):
    k = 0
    summ = 0
    for element in numbers:
        k += 1
        summ += element
    sr_znach = summ / k

    return sr_znach


def mediana(numbers):
    k = 0
    for element in numbers:
        k += 1

    return (numbers[(k)//2])


def moda(numbers):
    new_dict = {}
    list_values = []

    for i in numbers:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    for v in new_dict.values():
        list_values.append(v)
    return max(list_values)


dict_1 = {}
dict_1['mean'] = mean(numbers)
dict_1['median'] = mediana(numbers)
dict_1['mode'] = moda(numbers)
dict_1['sum'] = summa(numbers)
print(dict_1)
