class Figure:
    sides_count = 0
    def __init__(self, __color:list, *__sides:list):
        self.sides = list(__sides)
        self.color = __color
        print(self.sides)
        if len(self.sides) != 1:
            self.sides = 1
            print(self.sides)


    def get_sides(self):
        if isinstance(self.sides, list):
            self.sides = self.sides[0]
        list_ = []
        for i in range(self.sides_count):
            list_.append(self.sides)
        return list_

figure = Figure([15, 25, 23], 2, 3, 4)
print(figure.get_sides())
#
# figure.set_color(200, 100, 150)
# figure.get_color()
#
# figure.set_color(300, 100, 150)
# figure.get_color()
