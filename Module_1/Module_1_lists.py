'''Списки. Индексация и методы списков'''

food = ['apple', 'coconut', 'banana']
# print(food)
# print(food[0])
# food[0] = 'peach'
# print(food[0])
# print(food)
food.append(True) # Добавление элемента в конец списка
print(food)
food.
# food.extend('string')
# print(food)
# food.extend(['string'])
# print(food)
# food.remove('peach') # удаление элемента списка
# print(food)
#
# print('coconut' in food) # Проверка наличия элемента в списке
# print('apple' not in food) # Проверка отсутствия элемента в списке

# '''Кортежи'''
# tuple_1 = 1, 2, 3, True, 'String'
# print(tuple_1)
# tuple_2 = (1, 2, 3, 4)
# print(tuple_2)
# tuple_3 = tuple ([1, 2, 3, 4])
# print(tuple_3)
#
# # Кортеж так же, как и список, является коллекцией, но в отличие от него он неизменяем.
# # К неизменяемым объектам помимо кортежей относятся числа и строки.
#
# tuple_ = 1, 2, 3, 4
# print(tuple_)
# # tuple_1[0] = 15 # Выдаст ошибку изменит ь элемент кортежа нельзя
# # print(tuple_1)
#
# # Элементами кортежа могут быть изменяемые объекты, например списки
#
# tuple_ = [1, 2], 3, 4
# print(tuple_)
#
# # Теперь можно будет изменить элемент внутри вложенного в кортеж списка
# tuple_[0][0] = 5
# print(tuple_)
#
# # Операции поддерживаемые кортежами
# tuple_ = tuple_1 + tuple_2
# print(tuple_)
#
# tuple_ = tuple_2 * 3
# print(tuple_)
#
