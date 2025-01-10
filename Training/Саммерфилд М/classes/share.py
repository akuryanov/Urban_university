import math

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y) # возвращает длину многомерного вектора с координатами,
        # заданными в позиционных аргументах coordinates, и началом в центре системы координат.

    def __eq__(self, other):
        return self.x == other.x and self.y  == other.y # Возвращает True, если x(a) = x(b) и y(a) = y(b)

    def __repr__(self):
    # Метод __repr__ в Python выдает текстовое или строковое представление сущности или объекта.
    # Этот процесс вызывается всякий раз при вызове метода repr() для какой-то сущности.
    # Предназначен для предоставления «официального» текстового образа объекта,
    # который можно использовать для воссоздания этого объекта.
        return f'({self.x}, {self.y})'


    def __str__(self):
    # Функция __str__ в Python делает то же самое, что и __repr__, но ее поведение всё же немного отличается.
    # Она предназначена для создания удобочитаемой версии,
    # полезной для отслеживания или отображения информации об объекте
        return f'Point({self.x}, {self.y})'

a = Point()

print(repr(a))
b = Point(3, 4)

print(b)
print(b.distance_from_origin())
b.x = -19
print(b)

