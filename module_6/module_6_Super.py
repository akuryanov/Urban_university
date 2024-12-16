class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f'привет, меня зовут {self.name}')


class Student_Group:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')

class Student(Human, Student_Group):
    def __init__(self, name, place, group):
        super().__init__(name, group) # обращение к родительскому классу аналогично Human.__init__(self, name)
        self.place = place
        super().info()


print(Student.mro()) # Просмотр наследования
# human = Human('Денис')
# print(human.name)

student = Student('Макс', 'Урбан', 'Python-1')
# student.about()
# print(student.name, student.place)
