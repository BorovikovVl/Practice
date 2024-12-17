fruits_and_colors = {
    "apple": "red",
    "banana": "yellow",
    "mango": "yellow",
    "orange": "orange",
    "lemon": "yellow",
    "grape": "purple"
}

Yellow_fruits = []
for k, v in fruits_and_colors.items():
    if v == 'yellow':
        Yellow_fruits.append(k)
print('Yellow fruits: ', Yellow_fruits)
