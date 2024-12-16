class Human:
    head = True

    # def __init__(self):
    #     self.about()

    def sey_hello(self):
        print('Hello!')

class Student(Human): # В круглых скобках указывается от какого класса наследуется класс
                      # Human - базовый класс, Student - наследуется от Human

    def about(self):
        print('I am student')

class Teacher(Human):
    pass


# human = Human()
student = Student()
teacher = Teacher()
student.sey_hello()
teacher.sey_hello()

# print(human.head)
student.about()

print(student.head)
# human.about()
