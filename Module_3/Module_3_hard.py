def calculate_structure_sum(*args ):
    sum = 0
    for i in args: # проходим по всем элементам и проверяем элементы соответствию типам данных
        if isinstance(i, int): # Если находим числа, просто суммируем их
            sum += i
        if isinstance(i, str): # Если находим строку добавляем к сумме длину строки
            sum += len(i)
        if isinstance(i, list): # Если находим список, проходим по всем элементам списка
            for j in i:
                sum += calculate_structure_sum(j) # и суммируем элементы вызывая рекурсивную функцию
        if isinstance(i, tuple): # аналогично со списком, поступаем с кортежем
            for j in i:
                sum += calculate_structure_sum(j)
        if isinstance(i, set): # аналогично со списком, поступаем с множеством
            for j in i:
                sum += calculate_structure_sum(j)
        if isinstance(i, dict): # если находим словарь
            for key, value in i.items(): # проходим по всем элементам получая ключи и значения элементов
                sum += calculate_structure_sum(key) # к сумме добавляем длину ключа через реверсивную функцию
                sum += calculate_structure_sum(value) # к сумме добавляем значение ключа через реверсивную функцию
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вывод результата
result = calculate_structure_sum(*data_structure)
print(result)