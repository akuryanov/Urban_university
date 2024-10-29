'''Списки. Индексация и методы списков'''

food = ['apple', 'coconut', 'banana']
print(food)
print(food[0])
food[0] = 'peach'
print(food[0])
print(food)
food.append(True) # Добавление элемента в конец списка
print(food)

food.extend('string')
print(food)
food.extend(['string'])
print(food)
food.remove('peach') # удаление элемента списка
print(food)

print('coconut' in food) # Проверка наличия элемента в списке
print('apple' not in food) # Проверка отсутствия элемента в списке
