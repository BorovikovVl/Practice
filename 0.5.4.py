def reverse(dict):
    dict1 = {}
    for key, znach in dict.items():
        dict1[znach] = key
    return dict1


dict2 = {"a": 1, "b": 2, "c": 3}
print(reverse(dict2))
