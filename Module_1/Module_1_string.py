'''Строки и Индексация строк'''
# name = 'Alexandr'
# print('Строка', name)
# print('Сложение строк', name + name)
# print('Умножение строк', name * 5)
# print('Первый символ', name[0])
# print('Последний символ', name[-1])
# print('Диапазон', name[0:4]) # Последний элемент не включается в вывод
# print('Диапазон с шагом', name[0:6:2]) # Последний элемент не включается в вывод
# print('Диапазон с начала до 6 знака',name[:6]) # вывод всех элементов с 1-го до 6-го (индексы с 0 до 5)
# print('Диапазон c 4 знака до конца',name[3:]) # вывод всех элементов с 4-го до конца

'''Модуль 1. Практическое задание по уроку "Строки и индексация строк"'''
# exsample = 'Программирование'
# print(exsample[0])
# print(exsample[-1])
# number_of_characters = len(exsample)
# middle_of_line = number_of_characters // 2
# print(exsample[middle_of_line:])
# print(''.join(reversed(exsample)))
# print(exsample[0::2])


'''Организация программ и методы строк'''
# name = input('Ведите имя: ') # input всегда вводит значение типа string
# current_year = 2024
# date_of_birth = int(input('Введите год рождения: ')) # Преобразуем вводимую строку в число
# print('Здравствуйте,', name)
# age = current_year - date_of_birth
# print('В этом году', current_year, 'Вам', age)

# print('привет, я строка в нижнем регистре')
# print('привет, я строка переведенная в верхний регистр'.upper())
# print('ПРИВЕТ Я СТРОКА ПЕРЕВЕДЕННАЯ В НИЖНИЙ РЕГИСТР'.lower())
# print('привет, я строка в нижнем регистре'.replace('привет', 'пока')) # замена символов в строке на новые значения
#                                                                                   # сначала указываем что нужно заменить
#                                                                                   # потом, на что нужно заменить
# print('привет, я строка в нижнем регистре'.replace(' ', '__'))

'''Модуль 1. Практическое задание по уроку "Организация программ и методы строк"'''
# my_string = input('Введите строку: ')
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.replace(' ', ''))
# print(my_string[0])
# print(my_string[-1])

