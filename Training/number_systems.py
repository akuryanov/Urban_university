# ======================= Перевод числа из 10-ой системы счисления в систему счисления n (n < 9)
# def decimal_to_another (number, system):
#     result = ''
#     if system < 9:
#         while number > 0:
#             remains = number % system
#             number = number // system
#             result = str(remains) + result
#
#
#     return result
#
# number = int(input('Введите десятичное число: '))
# system = int(input('Введите систему счисления меньше 9: '))
# print(f'Десятичное число {number} в системе счисления {system} равно - ', decimal_to_another (number, system))


# ====================== Извлечение квадратного корня через площадь прямоугольника
# Суть алгоритма в получении из прямоугольника длина одной стороны которого равна квадрату числа квадрата той же площади
# с заданной точностью вычисления

def sqrt_(width, eps):
    height = 1
    s = width * height
    while abs(width - height) > eps: # Вычисление модуля разности чисел
        height = (width + height) / 2 # усреднение одной из сторон прямоугольника
        width = s / height # вычисление другой стороны прямоугольника

    else:
        return height

width = float(input('Введите число: '))
eps = float(input('Введите точность вычисления: '))

print(f'Квадратный корень числа {width}, равен:', sqrt_(width, eps))