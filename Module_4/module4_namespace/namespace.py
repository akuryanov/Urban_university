# import this # Правила Python
import  math
# Существует четыре области видимости
# Глобальная
# Встроенная
# Локальная
# Объемлющая

print('---------- import  math-------------')
d = 7
def square(x):
    # global d
    d = x ** 2
    def even(x):
        nonlocal d
        d = x / 2
        if d % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')
    even(x)
    # print(globals()) # Возвращает список атрибутов в глобальном пространстве имен
    # print(locals()) # Возвращает список атрибутов в локальном пространстве имен
    return d

a = 5
# print(math.sqrt(a))

b = square(3)
print(b)
# print(globals()) # Возвращает список атрибутов в глобальном пространстве имен

# ===============================================================================================

# from math import *
# a = 5
# print()
# print('---------- from math import *-------------')
# print(sqrt(a))
# print(globals()) # Возвращает список атрибутов в глобальном пространстве имен



# Глобальное пространство имен