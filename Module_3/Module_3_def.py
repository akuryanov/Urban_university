# Пространство имен
'''
Существует несколько видов пространства имен:
Локальное пространство имен
Глобальное пространство имен
Встроенное пространство имен
Встроенное пространство имен включает в себя имена каких-либо встроенных функций.
Локальное представляет собой имена, которые мы создаем самостоятельно и используем внутри каких-либо функций.
Глобальное пространство имен включает в себя все, что есть в нашей программе, исключая лишь локальное пространство.
'''

# def printer():
#     # локальное пространство имен
#     # global a, b # Определение глобальных переменных внутри функции. Будут использоваться после окончания работы функции
#
#     # локальное пространство имен
#     c = 15
#     d = 20
#     a = 'A'
#     b = 'B'
#     print('Локальные переменные', c, d)
#     print('Локальные переменные', a, b)
#     print('Глобальные переменные', i, j)
#
#
# # Глобальное пространство имен
# a = 27
# b = 30
# i = 20
# j = 20
#
# printer()
# print('Глобальные переменные', a, b)

# Распаковка позиционных параметров

'''
Одна “звездочка” используется для распаковки и запаковки именно позиционных параметров, 
которые содержат один элемент: списки, кортежи, множества и т.д.;

Две “звездочки” используются для запаковки и распаковки именованных параметров(рис.1). 
В Python такая коллекция одна - словари. В них элементы хранятся парами.
'''
# def print_params (a, b, c):
#     print(a, b, c)
#
# def print_params_1(*args):
#     print('Вывод ', type(args), *args)
#     print('Вывод ',type(args),  args)
#
# def print_params_2(**kwargs):
#     print('Вывод ', type(kwargs), *kwargs) # выводит только ключи словаря
#     print('Вывод ',type(kwargs),  kwargs) # выводит словарь
#     for key in kwargs:
#         print(key)
#
# list_ = [1, 2, 3]
# print_params(list_, 4, 5)
#
# print_params(*list_) # Распаковка передаваемого параметра
# print_params_1(list_)
# print_params_1(*list_) # Распаковка передаваемого параметра
#
# dict_ = {'a':1, 'b':2, 'c':3}
#
# print_params_2(**dict_)
# print_params_1(dict_)
# print_params_1(*dict_)
# print_params(**dict_)

# Произвольное число параметров

# def test_func(*params):
#     print('Тип', type(params))
#     print('Аргумент', params)
#
# test_func(1, 2, 3, 4)

# def summator(txt, *values, type = 'sum'):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type}'
#
# print(summator('Сумма чисел: ', 2, 3, 4, 5))
# print(summator('Сумма чисел: ', 2, 3, 4, 5, type = 'summator'))

'''
Есть возможность использовать все виды параметров при объявлении функции как: позиционное, 
параметры с переменным количеством, именованные параметры - параметры со значением по умолчанию. 
В том числе есть возможность использовать и произвольное число именованных параметров.
'''

# def test_info(**values):
#     print('Тип', type(values))
#     print('Аргумент', values)
#     for key, value in values.items(): # items() возвращает объект представления, который отображает список пар кортежей словаря (ключ, значение)
#         print(key, value)
#
# test_info(name = 'Den', course = 'Python')

'''
В том числе, если есть возможность использовать переменное количество именованных параметров, 
мы можем это комбинировать с переменным количеством позиционных параметров

!Единственное, что позиционные параметры никогда не идут после именованных
'''
# def test_info(value, *types, name_author ='Den', **values):
#     print('Тип', type(values))
#     print('Аргумент', values)
#     for key, value in values.items(): # items() возвращает объект представления, который отображает список пар кортежей словаря (ключ, значение)
#         print(key, value)
#     print(types)
#
# test_info('пример использования параметров всех типов', 1, 2, 3, 4, name_author='Denis', name = 'Den', course = 'Python')


# def my_sum(n, *args, txt = 'Сумма чисел'):
#     s = 0
#     for i in args:
#         s += i ** n
#     print(txt + ':',s)
#
# my_sum(1, 1, 2, 3, 4, 5)
# my_sum(2, 1, 2, 3, 4, 5, txt = 'Сумма квадратов')
# list_ = [2, 3, 4, 5, 6]
#
# my_sum(3, *list_, txt = 'Сумма кубов')


# Рекурсия
'''
Рекурсия — это такой способ определения функции или описание функции, когда эта самая функция вызывает саму себя.
'''
#
# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n-1)
#
# print(summa(5))

# Встроенные функции

# int()
# float()
# bool()
# str() - строка
# list() - список
# tuple() - кортеж
# dict() - словарь
# set() - множество
# input()
# round() - количество знаков после запятой
# salarys = [2300, 1800.48, 5000, 1234.8, 7500.12,]
# average = round(sum(salarys)/len(salarys), 2)
# print(f'Средняя зарплата - {average}')
# print(f'Максимальная зарплата - {round(max(salarys), 2)}')
# print(f'Минимальная зарплата - {round(min(salarys), 2)}')
# print('===========================')
# names_ = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
# zipped_list = list(zip(names_, salarys)) # Создаем список кортежей
# print(zipped_list)
# print('Зарплата Дениса - ', zipped_list[0])
# print('===========================')
# zipped_dict = dict(zip(names_, salarys)) # создаем словарь
# print(zipped_dict)
# print('Зарплата Дениса - ', zipped_dict['Денис'])

# # any()
# a = [True, False, False]
# print(any(a))
#
# a = [False, False, False]
# print(any(a))
#
# a = [1, 2, 0]
# print(any(a))
#
# a = [0, 0, 0]
# print(any(a))
#
# b = ''
# print(any(b))
# b = '0'
# print(any(b))
#
# # all()
#
# # dir()

'''
Практикум
'''
# def find_max(list_): # Нахожение максимального значения списка
#     max_ = list_[0]
#     for i in list_:
#         if i > max_:
#             max_ = i
#     return max_
#
# list_ = [-1, -3, 0, 8, 9, 0]
# print(find_max(list_))
#
# def count_even(list_): # Нахождение четных чисел в списке
#     counter = 0
#     for i in list_:
#         if i == 0:
#             continue
#         if i % 2 == 0:
#             counter += 1
#     return counter
#
# list_ = [-1, -4, 0, 8, 9, 0, 2, 4, 6, 5, 7, 2]
# print(count_even(list_))
#
# def unique(list_): # уникальный список
#     new_list_ = []
#     for i in list_:
#         if i not in new_list_:
#             new_list_.append(i)
#     return new_list_
#
# list_ = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# print(unique(list_))

'''==========================================================='''
