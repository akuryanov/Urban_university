import math

class Figure:
    sides_count = 0

    def __init__(self, __color: list, *__sides: list):
        self.sides = list(__sides)
        self.color = __color

        if len(self.sides) != 1:
            self.sides = 1

    def get_color(self):
        return list(self.color)

    def set_color(self,r, g, b):
        if self.__is_valid_color(r, g, b):
            self.color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        if type(r) == int and type(g) == int and type(b) == int:
            if (r >= 0 and r <= 255) and (g >= 0 and g <= 255) and (b >= 0 and b <= 255):
               return True

    def get_sides(self):
        if isinstance(self.sides, list):
            self.sides = self.sides[0]
        list_ = []
        for i in range(self.sides_count):
            list_.append(self.sides)
        return list_

    def __len__(self):

        if isinstance(self.sides, list):
            self.sides = self.sides[0]
        return self.sides * self.sides_count

    def set_sides(self, *new_sides: int):
        self.new_sides = new_sides

        if len(self.new_sides) == 1:
            self.sides = list(self.new_sides)
            return self.sides

class Circle(Figure):
    sides_count = 1

    def get_square(self):
        __radius = self.sides / (2 * math.pi)

        return f'Площадь круга {math.pi * __radius**2} кв. единиц'

class Triangle(Figure):
    sides_count = 3

    def set_square(self):
        return f'Площадь треугольника {(self.sides**2 * math.sqrt(3))/4} кв. единиц'


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return f'Объем куба: {self.sides ** 3} куб. единиц'

    def set_square(self):
        return f'Площадь куба {self.sides ** 2 * 6} кв. единиц'




print('КРУГ')
circle1 = Circle((200, 200, 100), 10, 12, 33)
print(f'Список сторон круга {circle1.get_sides()}')
circle1 = Circle((200, 200, 100), 10)
print(f'Список сторон круга {circle1.get_sides()}')
print(f'Периметр круга(длина окружности) {len(circle1)}')
circle1.set_sides(20)
print(f'Список сторон круга {circle1.get_sides()}')
circle1.set_sides(2, 3 ,4)
print(f'Список сторон круга {circle1.get_sides()}')
print(f'Периметр круга(длина окружности) {len(circle1)}')
print(circle1.get_square())
circle1.set_color(25,26,78)
print(f'Измененные цвета RGB {circle1.get_color()}')
circle1.set_color(300,200,150)
print(f'Измененные цвета RGB {circle1.get_color()}')

print()
print('КУБ')
cube1 = Cube((222, 35, 130), 4, 5, 6)
print(f'Список сторон куба {cube1.get_sides()}')
cube1 = Cube((222, 35, 130), 4)
print(f'Цвета куба {cube1.get_color()}')
print(f'Список сторон куба {cube1.get_sides()}')
print(f'Периметр куба: {len(cube1)}')
cube1.set_sides(5)
print(f'Список сторон куба {cube1.get_sides()}')
cube1.set_sides(5, 6, 7, 8)
print(f'Список сторон куба {cube1.get_sides()}')
print(cube1.get_volume())
print(cube1.set_square())
cube1.set_color(12, 25, 96)
print(f'Цвета куба {cube1.get_color()}')
cube1.set_color(12, 265, 96)
print(f'Цвета куба {cube1.get_color()}')


print()
print('ТРЕУГОЛЬНИК')
triangle = Triangle((222, 35, 130), 4, 3, 4)
print(f'Список сторон треугольника {triangle.get_sides()}')
triangle = Triangle((222, 35, 130), 4)
print(f'Список сторон треугольника {triangle.get_sides()}')
print(f'Периметр треугольника: {len(triangle)}')
triangle.set_sides(10)
print(f'Список сторон треугольника {triangle.get_sides()}')
print(f'Периметр треугольника: {len(triangle)} единиц')
print(triangle.set_square())
