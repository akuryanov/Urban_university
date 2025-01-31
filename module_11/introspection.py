# Интроспекция - это способность объекта в процессе выполнения программы получать информацию о своём типе,
# доступных атрибутах и методах, а также другую важную информацию,
# необходимую для выполнения дополнительных операций с объектом.
# Интроспекция включает в себя специальные методы и атрибуты,
# которые можно вызывать у почти каждого объекта, и с помощью которых, можно получить дополнительную информацию о нём.

from pprint import pprint
import sys
import pandas

import requests

# help(requests) # предоставляет информацию, которую разработчик заложил в библиотеку, функцию или класс, то есть выводит «docstrings»

# pprint(dir(requests)) # Выводит информацию в столбик
# help(pandas)
# pprint(dir(pandas))
#
# def my_function():
#     pass
#
# class My_Class:
#     def __init__(self):
#         self.my_attr = 11
#
#     def my_class_func(self, value):
#         self.my_attr = value
#         print(self.my_attr)
#
# my_obj = My_Class()
# attr_name = 'attribute'

# ------------------------- hasattr(), getattr()

# print(f'наличие атрибута attr_name - {hasattr(my_obj, attr_name)}') # hasattr - Проверка наличия атрибута
# print(f'наличие атрибута my_attr - {hasattr(my_obj, "my_attr")}')
# print(getattr(my_obj, 'my_attr')) # getattr - Получение атрибута

# print(help(getattr))

# print(getattr(my_obj, attr_name, 'Этого атрибута нет'))
#
# for attr_name in dir(requests):
#     attr = getattr(requests, attr_name)
#     print(attr_name, type(attr))


# for attr_name in dir(pandas):
#     attr = getattr(pandas, attr_name)
#     print(attr_name, type(attr))

# ------------------------- callable() - проверка на то, можем ли мы вызвать этот объект

# print(callable(my_obj))
# print(callable(my_obj.my_class_func))

# ------------------------- isinstance() - позволяет определить, является ли объект экземпляром какого-либо класса

# print(isinstance(my_obj, int))
# print(isinstance(my_obj, My_Class))
# print(isinstance(my_obj.my_class_func, str))
# print(isinstance(my_obj, My_Class))
#

# print(help(sys))
# print(sys.version)
# print(sys.version_info)
# print(sys.executable)
# print(sys.platform)

def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)

sys.setrecursionlimit(6000)
print(factorial(5000))