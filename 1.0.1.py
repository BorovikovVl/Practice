class Rectangle:
    def __init__(self, width, high):
        self.width = width
        self.high = high

    def square_fun(self):
        self.square = self.width * self.high
        self.perimetr = (self.width + self.high) * 2

    def size(self):
        return f'Размеры прямоугольника: {self.square}, {self.perimetr}'

    def print_size(self):
        return f'Ширина: {self.width}  Длина: {self.high}' '\n'


rectan = Rectangle(2, 3)

print(rectan.print_size(),
      rectan.square_fun(),
      rectan.size())
