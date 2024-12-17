def playing(questions):
    sum_points = 0
    kolvo_questions = []
    len_kolvo = 0

    for keys, values in questions.items():
        kolvo_questions.append(keys)
        len_kolvo = len(kolvo_questions)

    while len_kolvo > 0:
        for keys, value in questions.items():
            for k, v in value.items():
                print(keys)
                string = input()
                if string in k:
                    sum_points += int(v)
                    len_kolvo -= 1
                    print(f'Правильный ответ! Сумма баллов: {sum_points}')
                else:
                    print('Неправильный ответ')
                    len_kolvo -= 1

    return f'Ваши баллы за опрос: {sum_points} из 12'


def new_question(questions):
    new_string = input()
    new_answer = input()
    new_point = input()
    new_dict = {}

    new_dict[new_answer] = new_point
    questions[new_string] = new_dict

    return questions


questions = {'Кто проживет на дне океана?': {'Губка Боб Квадратные штаны': '3'},
             'Производная sin?': {'cos': '4'},
             'Президент России - это...': {'Владимир Вдадимирович Путин': '5'}
             }


print(playing(questions))
print(new_question(questions))
