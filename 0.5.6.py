people_info = {
    "Alice": {"age": 25, "city": "New York", "occupation": "Engineer"},
    "Bob": {"age": 30, "city": "Los Angeles", "occupation": "Designer"},
    "Charlie": {"age": 35, "city": "Chicago", "occupation": "Teacher"},
    "Diana": {"age": 28, "city": "Miami", "occupation": "Doctor"},
    "Ethan": {"age": 40, "city": "Seattle", "occupation": "Chef"},
    "Frank": {"age": 32, "city": "Atlanta", "occupation": "Lawyer"},
    "Gabriella": {"age": 29, "city": "San Francisco", "occupation": "Software Engineer"},
    "Harrison": {"age": 38, "city": "Denver", "occupation": "Architect"},
    "Isabella": {"age": 26, "city": "Washington D.C.", "occupation": "Journalist"},
    "Julian": {"age": 42, "city": "Miami", "occupation": "Musician"},
    "Kate": {"age": 31, "city": "Philadelphia", "occupation": "Nurse"},
    "Lucas": {"age": 36, "city": "Nashville", "occupation": "Businessman"},
    "Mia": {"age": 27, "city": "Atlanta", "occupation": "Artist"},
    "Natalie": {"age": 39, "city": "Portland", "occupation": "Writer"},
    "Oliver": {"age": 44, "city": "Minneapolis", "occupation": "Professor"},
    "Penelope": {"age": 33, "city": "San Diego", "occupation": "Marketing Manager"},
    "Quincy": {"age": 41, "city": "Nashville", "occupation": "Singer"},
    "Rachel": {"age": 34, "city": "Cleveland", "occupation": "Teacher"},
    "Sophia": {"age": 29, "city": "Nashville", "occupation": "Engineer"},
    "Tessa": {"age": 37, "city": "Miami", "occupation": "Lawyer"}
}

for k, v in people_info.items():
    kolvo = 0
    dict_occupation = {}
    if v['age'] > 30:
        print(k)

dict_city = {}
for k, v in people_info.items():
    for ke, i in v.items():
        if ke == 'city':
            if i not in dict_city:
                dict_city[i] = 1
            else:
                dict_city[i] += 1

        else:
            continue

dict_occupation = {}
new_list = []
for k, v in people_info.items():
    for ke, i in v.items():
        if ke == 'occupation':
            dict_occupation[i] = k
        else:
            continue


print(k)
print(dict_city)
print(dict_occupation)