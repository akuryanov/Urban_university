# ФУНКЦИИ
from random import random


# def hello():
#     print('Hello')
# hello()
#
#
# def hello_name(name):
#     print('Hello', name)
# name = 'Alex'
# hello_name(name)
# hello_name('Denis')

import random
# def lottery(mon, thue):
#     ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(ticket)
#     ticket.remove(win1)
#     win2 = random.choice(ticket)
#     print(mon, thue)
#     return win1, win2 # Возможен вывод нескольких значений

# def lottery(*args, **kwargs): # Если количество параметров неизвестно можно использовать *args для обычных параметров
#                               # **kwargs - для именованных параметров
#     ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(ticket)
#     ticket.remove(win1)
#     win2 = random.choice(ticket)
#     print(*args)
#     return win1, win2 # Возможен вывод нескольких значений
#
# win1, win2 = lottery(1, 2, 'mon', 'thue')
# print(win1, win2)

# def test(a = 2, b = True): # Функция может иметь параметры по умолчанию
#     print(a, b)
#
# test()
# test(False, 'Ok')
# test([1, 2])
# test(*[1, 2]) # распаковка списка Таким образом элемент списка «1» занял место параметра «а», а элемент списка «2» занял место параметра «b»


def test(a,  b): # Функция может иметь параметры по умолчанию
    print(a, b)

c = {'Alex': 1998, 'Lisa':2001}
test(*c)
#test(**c)