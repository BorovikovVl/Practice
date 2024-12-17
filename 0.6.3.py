def combination(keys, values):
    new_dict = {}
    for k in keys:
        for v in values:
            new_dict[k] = v
        return new_dict


keys = ['a', 'b', 'c', 'e']
values = [1, 2, 3, 4]
print(combination(keys, values))
