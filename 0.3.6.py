from random import choice

lil_words = ["игра", "компьютер", "питон", "груша"]
word = choice(lil_words)
shifr = '*' * len(word)

while shifr != word:
    answer = input("Угадывайте букву:")
    for i in range(len(word)-1):
        if answer == word[i]:
            shifr[i] = answer
            print(shifr)
        else:
            print('Нет такой буквы')

print(word)