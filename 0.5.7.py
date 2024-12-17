reviews = {}


def add_review(subject, rating, comment):
    reviews.setdefault(subject, []).append({'rating': rating, 'comment': comment})


def view_reviews(subject):
    if reviews.get(subject):
        print(f"Отзывы для '{subject}':")
        for idx, review in enumerate(reviews[subject], start=1):
            print(f"{idx}. Оценка: {review['rating']}, Комментарий: {review['comment']}")
    else:
        print(f"Отзывов для '{subject}' нет.")


def delete_review(subject, index):
    if 0 <= index < len(reviews.get(subject, [])):
        removed = reviews[subject].pop(index)
        print(f"Удален отзыв: Оценка {removed['rating']}, Комментарий: {removed['comment']}")
    else:
        print("Неправильный индекс.")


def calculate_average_rating(subject):
    if reviews.get(subject):
        average = sum(review['rating'] for review in reviews[subject]) / len(reviews[subject])
        print(f"Средний балл для '{subject}': {average:.2f}")
    else:
        print(f"Отзывов для '{subject}' нет.")


def get_int_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Ошибка: Введите число от {min_value} до {max_value}.")
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")


def main():
    while True:
        print("\nМеню:\n1. Добавить отзыв\n2. Просмотреть отзывы\n3. Удалить отзыв\n4. Вычислить средний балл\n5. Выход")
        choice = get_int_input("Выберите действие (1-5): ", 1, 5)

        if choice == 1:
            subject = input("Введите название предмета: ")
            rating = get_int_input("Введите оценку (от 1 до 5): ", 1, 5)
            comment = input("Введите текст отзыва: ")
            add_review(subject, rating, comment)
            print("Отзыв добавлен.")

        elif choice == 2:
            subject = input("Введите название предмета для просмотра отзывов: ")
            view_reviews(subject)

        elif choice == 3:
            subject = input("Введите название предмета для удаления отзыва: ")
            view_reviews(subject)
            if subject in reviews:
                index = get_int_input("Введите номер отзыва для удаления: ", 1, len(reviews[subject])) - 1
                delete_review(subject, index)

        elif choice == 4:
            subject = input("Введите название предмета для вычисления среднего балла: ")
            calculate_average_rating(subject)

        else:
            print("Выход из программы.")
            break


if __name__ == "__main__":
    main()