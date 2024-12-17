class Employee():
    def __init__(self, exp_of_work, education, start_salary):
        self.exp_of_work = exp_of_work
        self.education = education
        self.start_salary = start_salary


class Manager(Employee):
    def __init__(self, exp_of_work, education, amount_of_work, start_salary):
        # Начальная зп всегда = 0
        self.amount_of_work = amount_of_work
        super().__init__(exp_of_work, education, start_salary)

    def salary(self):
        if self.exp_of_work > 3:
            self.start_salary = 30000
        else:
            self.start_salary = 15000
        if 'высшее' in self.education:
            self.start_salary += 18000
        else:
            self.start_salary += 9000
        if 'большой объем' in self.amount_of_work:
            self.start_salary += 10000
        else:
            self.start_salary += 2000
        return f'Зарплата манагера = {self.start_salary}'


class Developer(Employee):
    def __init__(self, exp_of_work, education, work_online, start_salary):
        # Начальная зп всегда = 0
        self.work_online = work_online
        super().__init__(exp_of_work, education, start_salary)

    def salary(self):
        if self.exp_of_work > 4:
            self.start_salary = 52000
        else:
            self.start_salary = 32000
        if 'высшее' in self.education:
            self.start_salary += 35000
        else:
            self.start_salary += 15000
        if self.work_online > 25:
            self.start_salary += 20000
        else:
            self.start_salary += 5000
        return f'Зарплата девелопера = {self.start_salary}'


manag = Manager(4, 'среднее', 'мало', 0)
print(manag.salary())

developer = Developer(4, 'высшее', 26, 0)
print(developer.salary())
