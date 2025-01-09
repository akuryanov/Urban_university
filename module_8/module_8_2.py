
def personal_sum (numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i

        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы - {i}')

    return result, incorrect_data

def calculate_average(numbers):
    try:
        result = personal_sum(numbers)
        if result[0] == 0:
            result = 0
        else:
            result = result[0] / (len(numbers) - result[1])
        return result
    except ZeroDivisionError:
        print('Передана пустая коллекция')
    except TypeError:
        print('В numbers  записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
