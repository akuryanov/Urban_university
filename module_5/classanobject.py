# Класс - создает собственный тип данных
# Атрибуты представляют собой переменные внутри класса,
# а методы — функции, определенные внутри него
# self является указателем на сам объект


class Human:
    def __init__(self, name, age): # Конструктор класса
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня сегодня День рождения, мне теперь {self.age}')


den = Human('Денис', 22)
max = Human('Максим', 23)

# Атрибуты, или характеристики, можно задавать и вручную
den.surname = 'Попов'
print(den.surname)
# Таким образом, был добавлен атрибут, который не задается при инициализации,
# то есть не при создании объекта, а возникает в процессе работы программы.

# print(type(den))
# print(den.name, den.age)
# print(max.name, max.age)
# den.say_info()
# max.say_info()
# birthday()
max.birthday()

