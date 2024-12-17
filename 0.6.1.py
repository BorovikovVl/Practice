def clear(somelist):
    list1 = []
    for element in somelist:
        if element not in list1:
            list1.append(element)
    return list1


vvod = input()
somelist = vvod.split()
print(clear(somelist))
