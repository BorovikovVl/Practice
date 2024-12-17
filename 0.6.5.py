def find_maxim(some_dict):
    max_k = 0
    max_v = 0
    for k, v in some_dict.items():
        if v > max_v:
            max_k = k
            max_v = v

    return max_k


sentence = ('Страдание и боль всегда обязательны для широкого сознания и глубокого сердца.')
somelist = sentence.split()
k = 0
some_dict = {}
list_values = []
for word in somelist:
    for letter in word:
        k += 1
    some_dict[word] = k
    k = 0

print(find_maxim(some_dict))

