def spisok_kolvo(element):
    main_list = {}
    k = 0
    list_element = element.split(' ')
    for el in list_element:
        if el not in list_element:
            k = 1
            main_list[el] == k
            k += 1
        else:
            k += 1
            main_list[el] == k
    return main_list


element = input()
print(spisok_kolvo(element))