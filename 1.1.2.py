class Transport():
    def __init__(self, lenght, speed):
        self.lenght = lenght
        self.speed = speed


class Auto(Transport):
    def __init__(self, lenght, speed, brand_car):
        self.brand_car = brand_car
        super().__init__(lenght, speed)

    def description(self):
        return f'Длина машины: {self.lenght}      Скорость машины: {self.speed}\
        Марка машины: {self.brand_car}'


class Bus(Transport):
    def __init__(self, lenght, speed, generation):
        self.generation = generation
        super().__init__(lenght, speed)

    def description(self):
        return f'Длина автобуса: {self.lenght}      Скорость автобуса: {self.speed}\
        Поколение автобуса: {self.generation}'


class Trolleybus(Transport):
    def __init__(self, lenght, speed, people):
        self.people = people
        super().__init__(lenght, speed)

    def description(self):
        return f'Длина троллейбуса: {self.lenght}      Скорость троллейбуса: {self.speed}\
        Кол-во людей: {self.people}'


auto = Auto(3, 100, 'zhiga')
print(auto.description())
print('=======================================================================')

bus = Bus(7, 60, 2)
print(bus.description())
print('=======================================================================')

trolleybus = Trolleybus(5, 55, 32)
print(trolleybus.description())
