# from sortfunc import *
import sortfunc

#
# Метод split создает список из строки
# Функция map позволяет применить int к каждому элементу строки
# list превращает все в список

data_1 = list(map(int, input('Введите числа через пробел: ').split()))
data_2 = list(map(int, input('Введите числа через пробел: ').split()))
data_3 = list(map(int, input('Введите числа через пробел: ').split()))

sortfunc.bubble_sort(data_1)
sortfunc.selected_sort(data_2)
sortfunc.insertion_sort(data_3)

print('Пузырьковая сортировка',data_1)
print('Сортировка выбором',data_2)
print('Сортировка вставкой',data_3)

