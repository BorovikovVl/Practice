def info(student, grade):
    grade = grade.split(' ')
    dict_students[student] = 0
    print(f'Фамилия студента: {student}')
    print(f'Оценки: {grade}')


def average_grade(grade):
    grades = grade.split(' ')
    sum_grade = 0

    for i in grades:
        sum_grade += int(i)

    len_grade = len(grades)
    average_grades = sum_grade / len_grade
    dict_students[student] = average_grades
    print(f'Средний балл студента: {average_grades:.2f}')


def students_inf(dict_students):
    print(dict_students)


def find(dict_students):
    for k, v in dict_students.items():
        if k in dict_students:
            print(v)
        else:
            print('Такого студента нет в данных')


dict_students = {}
student = input()
grade = input()
print('-------------------')

info(student, grade)
average_grade(grade)
students_inf(dict_students)
find(dict_students)
