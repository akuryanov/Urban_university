# Функциональное программирование
#
# def get_russian_names():
#     print(['Ваня', 'Коля', 'Маша', ])
#
# get_russian_names()
# print(type(get_russian_names))
# print(get_russian_names.__name__)
#
# my_func = get_russian_names
# print(my_func())
# print(my_func.__name__)


#=====================================================

# my_numbers = [3, 1, 4 , 1, 5, 9, 2, 6]
#
# # Функция map() применяет функцию к каждому элементу последовательности и формирует список результатов
#
# def mul_by_2(x):
#     return x * 2
#
# result = map(mul_by_2, my_numbers)
# print(list(result))
#
# # Функция filter() вычисляет функцию для каждого элемента последовательности
# # и добавляет элемент, если функция верна
#
# def is_odd(x):
#     return x % 2
#
# result = filter(is_odd, my_numbers)
#
# print(list(result))
#
# # Списковые сборки
#
# result = map(mul_by_2, filter(is_odd, my_numbers))
# print(list(result))
#
# list_comp_1 = [x*3 for x in my_numbers]
# print(list_comp_1)
#
# list_comp_2 = [x*2 for x in my_numbers if x > 5] # фильтрация элементов
# print(list_comp_2)
#
# list_comp_3 = [x*3 for x in my_numbers if x % 2]
# print(list_comp_3)
#
# list_comp_4 = [x*2 if x > 2 else x*10 for x in my_numbers] # проверка элементов и выполнение разных
#                                                            # действий в зависимости от результата проверки
# print(list_comp_4)

#=====================================================
# Вложенные списки
#
# collection_1 = [1, 2, 3, 4, 5]
# collection_2 = [3, 5, 6, 8, 9]
# list_comp_5 = [x * y for  x in collection_1 for y in collection_2]
# print(list_comp_5)
#
# list_comp_5 = [x * y for  x in collection_1 for y in collection_2 if x % 2]
# print(list_comp_5)
#
# list_comp_5 = [x * y for  x in collection_1 for y in collection_2 if x % 2 and y // 2]
# print(list_comp_5)
#
# # Множества
# my_numbers = [3, 1, 4 , 1, 5, 9, 2, 6]
# result = {x for x in my_numbers}
# print(result)
#
# # Словари
# result = {x: x**2 for x in my_numbers}
# print(result)

#=====================================================
# Генераторные сборки

# my_numbers = [3, 1, 4 , 1, 5, 9, 2, 6]
# result = (x ** 100 for x in my_numbers) # Пример генераторной сборки
#
# print(result)

#=====================================================
# Итераторы
import sys
from itertools import repeat

ex_iterator = repeat('4', 100_000)
print(ex_iterator)
print(f'Размер итератора - {sys.getsizeof(ex_iterator)}')

ex_str = '4'* 100_000
print(f'Размер списка - {sys.getsizeof(ex_str)}')




