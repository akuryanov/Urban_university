class Human:
    head = True
    _legs = True # _ перед именем делает это имя только для локального использования
    __arms = True # __ защищает имя от переопределения в дочерних классах

    # def __init__(self):
    #     self.about()

    def sey_hello(self):
        print('Hello!')

    def about (self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

class Student(Human): # В круглых скобках указывается от какого класса наследуется класс
                      # Human - базовый класс, Student - наследуется от Human
    pass
    # def about(self):
    #     print('I am student')

class Teacher(Human):
    pass


human = Human()
student = Student()
# teacher = Teacher()
# student.sey_hello()
# teacher.sey_hello()

# print(human.head)
student.about()

# print(student.head)
human.about()
print(dir(human))
