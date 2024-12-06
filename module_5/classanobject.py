# Класс - создает собственный тип данных
# Атрибуты представляют собой переменные внутри класса,
# а методы — функции, определенные внутри него
''' self - обязательный аргумент, содержащий в себе экземпляр класса,
    передающийся при вызове метода, поэтому этот аргумент должен присутствовать во всех методах класса

'''


#
class Human:
    head = True # Атрибут класса

    def __init__(self, name, age):  # Конструктор класса
        self.name = name  # Атрибут объекта класса
        self.age = age  # Атрибут объекта класса
        self.say_info()


    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня сегодня День рождения, мне теперь {self.age}')

    def __len__(self):
        return self.age # Возвращаем возраст

    def __str__(self): # ПЭтот метод определяет строковое представление нашего объекта
        return f'Привет, меня зовут {self.name}'

    # Перегрузка операторов
    # Часто в операциях участвуют два объекта.
    # Например, при сравнении одного человека с другим или одного числа с другим.
    # В операциях, таких как вычитание, сложение или умножение, также принимают участие два элемента.
    # В этом контексте можно представить, что self — это один участник операции, а other — второй

    def __lt__(self, other): # Метод '__lt__()' можно интерпретировать как «меньше чем» (Lower than)
        return self.age < other.age # Возвращает True если условие выполняется

    def __gt__(self, other): # Метод '__gt__()' интерпретируется как «больше чем» (Greater than)
        return self.age > other.age  # Возвращает True если условие выполняется

    def __eq__(self, other): # можно реализовать перегрузку оператора равенства с помощью метода '__eq__()'.
        # Этот метод проверяет, равен ли 'self.age' значению 'other.age'
        return self.name == other.name and self.age == other.age  # Возвращает True если условие выполняется



    def __del__(self):  # Деструктор класса удаляет объекты из памяти
            print(f'{self.name} ушёл')


den = Human('Денис', 22)
max = Human('Максим', 22)

# del den

# Атрибуты, или характеристики, можно задавать и вручную
# den.surname = 'Попов'
# print(den.surname)
# Таким образом, был добавлен атрибут, который не задается при инициализации,
# то есть не при создании объекта, а возникает в процессе работы программы.

print(type(den))
print(den.name, den.age)
# print(max.name, max.age)
# den.say_info()
# max.say_info()
# birthday()
# print(den)
# print(den < max)
# max.birthday()
# print(den < max)

# print(Human.head)
#
# # print(Human.__dict__)
#
# print('Атрибуты экземпляра den', den.__dict__)
# print('Атрибуты экземпляра max', max.__dict__)
#
#
# den.head = False # Создан атрибут экземпляра den
# print(den.head)
#
# print('Атрибуты экземпляра den', den.__dict__)
# print('Атрибуты экземпляра max', max.__dict__)



# Класс Object и магический метод '__new__()'.

# print(int.__mro__) # Отражает цепочку наследования


# class User:
#     def __new__(cls, *args, **kwargs):
#         print('Я в new')
#         return super().__new__(cls)  # Создание нового экземпляра с соответствующими аргументами
#
#     def __init__(self):
#         print('Я в init')
#
#
# user1 = User()
# user2 = User()
#
# print(id(user1), id(user2))
#
# # print(User.__mro__)

