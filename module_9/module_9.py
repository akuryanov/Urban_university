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

my_numbers = [3, 1, 4 , 1, 5, 9, 2, 6]

# Функция map() применяет функцию к каждому элементу последовательности и формирует список результатов

def mul_by_2(x):
    return x * 2

result = map(mul_by_2, my_numbers)
print(list(result))

# Функция filter() вычисляет функцию для каждого элемента последовательности
# и добавляет элемент, если функция верна

def is_odd(x):
    return x % 2

result = filter(is_odd, my_numbers)

print(list(result))


